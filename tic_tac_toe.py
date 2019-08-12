import itertools
import random

ASCII_TABLE = "     |     |     \n" \
              "     |     |     \n" \
              "_____|_____|_____\n" \
              "     |     |     \n" \
              "     |     |     \n" \
              "_____|_____|_____\n" \
              "     |     |     \n" \
              "     |     |     \n" \
              "     |     |     \n" \
              "\n" \
              "  TIC-TAC-TOE\n"


class Table(object):

    def __init__(self):
        self.grid = list(range(1, 10))
        self.table_representation = ASCII_TABLE
        self.win_combinations = [
            [1, 2, 3],
            [1, 4, 7],
            [1, 5, 9],
            [2, 5, 8],
            [3, 6, 9],
            [3, 5, 7],
            [4, 5, 6],
            [7, 8, 9],
        ]

    def mark_ascii_cell(self, grid_place, player_mark):
        return {
            1: self._replace_cell(21, grid_place, player_mark),
            2: self._replace_cell(27, grid_place, player_mark),
            3: self._replace_cell(33, grid_place, player_mark),
            4: self._replace_cell(75, grid_place, player_mark),
            5: self._replace_cell(81, grid_place, player_mark),
            6: self._replace_cell(87, grid_place, player_mark),
            7: self._replace_cell(129, grid_place, player_mark),
            8: self._replace_cell(135, grid_place, player_mark),
            9: self._replace_cell(141, grid_place, player_mark),
        }

    def _replace_cell(self, ascii_place, grid_place, player_mark):
        return self.table_representation[:ascii_place - 1] + \
            player_mark + self.table_representation[ascii_place:]

    def occupy_cell(self, grid_place, player_mark):
        self.grid.remove(grid_place)
        self.table_representation = self.mark_ascii_cell(grid_place, player_mark).get(grid_place)


class AbstractPlayer(object):

    def __init__(self, mark, name=None, human=False):
        self.human = human
        self.owned_cells = []
        self.name = name or "AI" + str(random.randint(1, 10))
        self.mark = mark

    def _check_if_win(self):
        if table.grid:
            c = itertools.combinations(self.owned_cells, 3)

            for combination in c:
                if list(combination) in table.win_combinations:
                    print("Player " + self.name + " wins!")
                    print(table.table_representation)
                    exit(0)

    def move(self, N=None):
        self._occupy_cell(N)
        self._finish_move(N)

    def _occupy_cell(self, N):
        raise NotImplementedError("You must define the way"
                                  "to occupy a cell on the"
                                  "grid")

    def _finish_move(self, N):
        self.owned_cells.append(N)
        self.owned_cells.sort()
        self._check_if_win()
        print(table.table_representation)


class HumanPlayer(AbstractPlayer):

    def _occupy_cell(self, N):
        if N in table.grid and 0 < N < 10:
            table.occupy_cell(N, self.mark)
        else:
            print("You are choosing an occupied cell or a non existing one")


class AIPlayer(AbstractPlayer):

    def _occupy_cell(self, N):
        auto_choice = random.choice(table.grid)
        table.occupy_cell(auto_choice)
        print("Player " + self.name + " chooses " + str(auto_choice) + ".")


def main():
    global table
    table = Table()
    start = None
    print(ASCII_TABLE)

    while not start:
        players = int(input("How many human players will play? (0-2): "))

        if 0 <= players < 3:
            if players == 0:
                player1 = AIPlayer(mark='X')
                player2 = AIPlayer(mark='O')
            elif players == 1:
                name = input("Please type the name of the player: ")
                player1 = HumanPlayer('X', name, True)
                player2 = AIPlayer(mark='O')
            elif players == 2:
                name = input("Please type the name of the first player: ")
                player1 = HumanPlayer('X', name, True)
                name = input("Please type the name of the second player: ")
                player2 = HumanPlayer('O', name, True)
            start = True

    for turn in range(9):
        if turn % 2 == 0:
            N = int(input("Please choose a cell " + player1.name + ": ")
                    ) if player1.human else None
            player1.move(N)
        else:
            N = int(input("Please choose a cell " + player2.name + ": ")
                    ) if player2.human else None
            player2.move(N)

    print("What a match, we have a draw!")
    print(table.table_representation)


if __name__ == "__main__":
    main()

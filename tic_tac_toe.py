import itertools
import random

from players import AbstractPlayer


class Table(object):

    def __init__(self):
        self.grid = range(1, 10)
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

    def occupy_cell(self, N):
        self.grid.remove(N)


class AbstractPlayer(object):

    def __init__(self, name=None, human=False):
        self.human = human
        self.owned_cells = []
        self.name = name or "AI" + str(random.randint(1, 10))

    def _check_if_win(self):
        if table.grid:
            c = itertools.combinations(self.owned_cells, 3)

            for combination in c:
                if list(combination) in table.win_combinations:
                    print("Player " + self.name + " wins!")
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


class HumanPlayer(AbstractPlayer):

    def _occupy_cell(self, N):
        if N in table.grid and 0 < N < 10:
            table.occupy_cell(N)
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

    while not start:
        players = int(raw_input("How many human players will play? (0-2): "))

        if 0 <= players < 3:
            if players == 0:
                player1 = AIPlayer()
                player2 = AIPlayer()
            elif players == 1:
                name = raw_input("Please type the name of the player: ")
                player1 = HumanPlayer(name, True)
                player2 = AIPlayer()
            elif players == 2:
                name = raw_input("Please type the name of the first player: ")
                player1 = HumanPlayer(name, True)
                name = raw_input("Please type the name of the second player: ")
                player2 = HumanPlayer(name, True)
            start = True

    for turn in range(9):
        if turn % 2 == 0:
            N = int(raw_input("Please choose a cell " + player1.name + ": ")
                    ) if player1.human else None
            player1.move(N)
        else:
            N = int(raw_input("Please choose a cell " + player2.name + ": ")
                    ) if player2.human else None
            player2.move(N)

    print("What a match, we have a draw!")


if __name__ == "__main__":
    main()

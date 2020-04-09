from random import random
from sys import stdout
from time import sleep

class Game:
  def __init__(self, size):
    self.size = size
    self.grid = self.create_grid()

  def stringify(self):
    rep = '\n'
    for row in self.grid:
      for val in row:
        rep += val
        rep += '   '
      rep += '\n'
    return rep

  def create_grid(self):
    n = self.size
    grid = []
    for i in range(n):
      row = [''] * n
      grid.append(row)
      for j in range(n):
        if random() <= 0.5:
          grid[i][j] = '*'
    return grid

  def check_neighbors(self, i, j):
    n = self.size
    count = 0
    coords = [((i + 1) % (n - 1), j), ((i + 1) % (n - 1), (j + 1) % (n - 1)), (i, (j + 1) % (n - 1)), (abs(i - 1) % (n - 1), (j + 1) % (n - 1)), 
              (abs(i - 1) % (n - 1), j), (abs(i - 1) % (n - 1), abs(j - 1) % (n - 1)), (i, abs(j - 1) % (n - 1)), ((i + 1) % (n - 1), abs(j - 1) % (n - 1))]
    for (x, y) in coords:
      if self.grid[x][y] == '*':
        count += 1
    return count

  def update(self):
    n = self.size
    for i in range(n):
      for j in range(n):
        count = self.check_neighbors(i, j)
        if count < 2 or count > 3:
          self.grid[i][j] = ''
        elif count == 3:
          self.grid[i][j] = '*'


if __name__ == '__main__':
  game = Game(10)
  for i in range(100):
    sleep(0.1)
    stdout.write(game.stringify())
    stdout.flush()
    game.update()

# Game of Life

Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

* Any live cell with two or three neighbors survives.
* Any dead cell with three live neighbors becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.


To run the script, specify the size of n x n grid and number of iterations.
For a 10 x 10 grid and 300 iterations run:
```
python game_of_life.py 10 300
```
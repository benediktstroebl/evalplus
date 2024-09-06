import math
def max_fill(grid, capacity):
    filled_rows = sum(list(accumulate(row)) for row in grid)
    return math.ceil(filled_rows / capacity)
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
import math
def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    return math.ceil(filled_rows / capacity)
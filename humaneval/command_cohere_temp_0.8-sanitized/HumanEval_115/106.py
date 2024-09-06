import math
def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(row) > 0)
    return math.ceil(filled_rows / capacity)
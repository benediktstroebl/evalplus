import math
def max_fill(grid, capacity):
    wells_filled = sum(sum(row) for row in grid)
    return math.ceil(wells_filled / capacity)
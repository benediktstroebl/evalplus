import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = sum(sum(row) for row in grid)
    return math.ceil(filled_wells / capacity)
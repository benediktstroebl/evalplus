import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(sum(row) for row in grid)
    max_fills = filled_rows + (rows - filled_rows) // math.ceil(capacity / wells)

    return max_fills
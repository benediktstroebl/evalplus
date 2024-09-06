import math
def max_fill(grid, capacity):
    wells, height = len(grid), len(grid[0])
    fills = 0

    for row in grid:
        max_row = max(row)
        fills += max_row * height

    return max(fills, capacity)
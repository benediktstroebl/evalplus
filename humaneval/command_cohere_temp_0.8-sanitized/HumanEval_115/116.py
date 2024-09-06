import math
def max_fill(grid, capacity):
    wells, height = len(grid), len(grid[0])
    fills = 0
    for x in range(wells):
        for y in range(height):
            if grid[x][y] == 1:
                fills += math.ceil(min(x + y, capacity))
    return fills
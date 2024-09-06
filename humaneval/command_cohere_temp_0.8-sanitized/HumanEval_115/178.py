import math
def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fills = [0] * wells
    for i in range(wells):
        fill = 0
        for j, val in enumerate(grid[i]):
            if val:
                fill += math.ceil(j / capacity)
        fills[i] = fill
    return max(fills)
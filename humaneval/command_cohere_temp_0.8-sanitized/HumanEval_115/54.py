import math
def max_fill(grid, capacity):
    wells, w = len(grid), 0
    while wells > 0:
        col, rem = 0, capacity
        for i in range(wells):
            col += grid[i][w]
            rem = min(rem, grid[i][w])
        w += rem
        wells -= math.ceil(col / capacity)
    return w
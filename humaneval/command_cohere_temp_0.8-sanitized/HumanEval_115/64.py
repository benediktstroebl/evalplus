import math
def max_fill(grid, capacity):
    wells, w = len(grid), 0
    for r in range(wells):
        bucket = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                bucket += 1
                if bucket >= capacity:
                    w += bucket // capacity
                    bucket %= capacity
        if bucket > 0:
            w += bucket // capacity
    return w
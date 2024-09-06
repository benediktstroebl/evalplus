import math
def max_fill(grid, capacity):
    wells, w_len = len(grid), len(grid[0])
    fills = []
    for row in grid:
        filled, c = 0, capacity
        for i in range(w_len):
            if row[i] == 1:
                filled += 1
                c -= 1
                if not c:
                    filled = 0
                    c = capacity
        fills.append(filled)
    return max(fills)
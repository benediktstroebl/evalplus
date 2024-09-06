import math
def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fills = [[0] * w for _ in range(wells)]

    for r in range(wells):
        for c in range(w):
            if grid[r][c] == 1:
                for i in range(r, wells):
                    for j in range(c, w):
                        if grid[i][j] == 1:
                            fills[r][c] = max(fills[r][c], 1 + min(capacity, fills[i][j]))

    return max(fills[-1])
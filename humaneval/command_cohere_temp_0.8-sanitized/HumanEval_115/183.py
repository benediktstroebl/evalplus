import math
def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fills = [[0 for _ in range(w)] for _ in range(wells)]
    max_fill_count = 0
    
    for r in range(wells):
        for c in range(w):
            if grid[r][c] == 1:
                for i in range(r, wells):
                    for j in range(c, w):
                        if grid[i][j] == 1:
                            fills[r][c] = max(fills[r][c], fills[i][j] + 1)
                            max_fill_count = max(max_fill_count, fills[r][c])
    
    return max_fill_count
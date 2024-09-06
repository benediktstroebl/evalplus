import math
def max_fill(grid, capacity):
    wells, rows = len(grid), len(grid[0])
    fills = [[0 for _ in range(rows)] for _ in range(wells)]
    
    for i in range(wells):
        for j in range(rows):
            if grid[i][j] == 1:
                fills[i][j] = math.inf
    
    for i in range(wells):
        for j in range(rows - 1, -1, -1):
            if grid[i][j] == 1:
                fills[i][j] = min(fills[i][j + 1], fills[i][j])
    
    return sum(max(min(fills[i][j] for j in range(rows)), capacity) for i in range(wells))
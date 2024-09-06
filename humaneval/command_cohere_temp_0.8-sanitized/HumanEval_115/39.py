import math
def max_fill(grid, capacity):
    wells, w_len = len(grid), len(grid[0])
    fills = []
    
    for i in range(wells):
        row = grid[i]
        fill = 0
        for j in range(w_len):
            if row[j] == 1:
                fill += math.ceil(j / capacity)
        fills.append(fill)
    
    return max(fills)
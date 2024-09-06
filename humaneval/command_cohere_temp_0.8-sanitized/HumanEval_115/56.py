import numpy as np
def max_fill(grid, capacity):
    grid = np.array(grid)
    fill = 0
    
    for i in range(grid.shape[0]):  # loop over rows
        row_sum = np.sum(grid[i])  # sum of units of water in the current row
        for j in range(row_sum, 0, -1):  # loop over units of water in the current row
            if capacity >= j:
                capacity -= j
                fill += 1
            else:
                fill += (j - capacity) // (j // capacity + 1)
                break
    
    return fill
capacity = 1
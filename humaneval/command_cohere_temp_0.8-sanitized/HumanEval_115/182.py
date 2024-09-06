import math
def max_fill(grid, capacity) :
    wells = len(grid)
    units = len(grid[0])
    filled = 0
    max_filled = 0
    for i in range(wells) :
        for j in range(units) :
            filled += grid[i][j]
        max_filled = max(max_filled, filled)
        filled = 0
    if max_filled >= capacity :
        return max_filled // capacity
    return max_filled // capacity + 1
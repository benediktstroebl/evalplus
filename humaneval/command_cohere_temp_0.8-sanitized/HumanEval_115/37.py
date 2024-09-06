import math
def max_fill(grid, capacity) :
    wells = len(grid)
    units = len(grid[0])
    filled_buckets = 0
    for i in range(wells) :
        for j in range(units) :
            if(grid[i][j] == 1) :
                filled_buckets += math.ceil(j / capacity)
    return filled_buckets
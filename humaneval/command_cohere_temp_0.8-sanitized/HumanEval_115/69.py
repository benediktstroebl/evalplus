import math
def max_fill(grid, capacity):
    filled_buckets = 0
    for i in range(len(grid)): # iterate over each well
        for j in range(len(grid[i])): # iterate over each column of the well
            if grid[i][j] == 1:
                filled_buckets += math.ceil(j / capacity)
    return filled_buckets
grid = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
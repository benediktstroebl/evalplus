import math
def max_fill(grid, capacity) :
    filled_buckets = 0
    row, col = len(grid), len(grid[0])
    for i in range(row) :
        filled_buckets += math.ceil(sum(grid[i]) / capacity)
    return filled_buckets
capacity = 1
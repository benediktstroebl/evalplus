import math
def max_fill(grid, capacity) :
    filled_buckets = 0
    for i in range(len(grid)) :
        row = grid[i]
        for j in range(len(row)) :
            if row[j] == 1 :
                filled_buckets += math.ceil(j / capacity)
    return filled_buckets
import math
def max_fill(grid, capacity):
    count = 0

    for i in range(len(grid)):
        row = grid[i]
        bucket = 0
        for j in range(len(row)):
            if row[j] == 1:
                bucket += 1
                if bucket == capacity:
                    count += math.ceil(bucket / capacity)
                    bucket = 0
        if bucket > 0:
            count += math.ceil(bucket / capacity)

    return count
capacity = 1
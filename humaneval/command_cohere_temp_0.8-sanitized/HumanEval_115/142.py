import math
def max_fill(grid, capacity):
    buckets = 0
    for row in grid:
        current_bucket = 0
        for col in row:
            if col == '1':
                current_bucket += 1
                if current_bucket == capacity:
                    buckets += 1
                    current_bucket = 0
        if current_bucket != 0:
            buckets += current_bucket

    return buckets
capacity = 1
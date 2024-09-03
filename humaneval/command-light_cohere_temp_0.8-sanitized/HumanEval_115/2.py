import math
def max_fill(grid, capacity):
    n = len(grid)
    rows = [0] * n
    buckets = [0] * n
    for i in range(n):
        rows[i] = grid[i][0]
        buckets[i] = math.max(rows[i])

    max_bucket = 0
    for i in range(n):
        if buckets[i] > max_bucket:
            max_bucket = buckets[i]
    return max_bucket
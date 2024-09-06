import math
def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    max_fill_count = filled_rows // capacity
    buckets = max_fill_count * capacity
    
    for row in grid:
        bins = 0
        for j in range(len(row)):
            if row[j] == 1:
                bins += 1
                if bins > capacity:
                    buckets += bins // capacity
                    bins = capacity
            else:
                bins = 0
        buckets += bins
    
    return buckets
import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)

    filled_buckets = sum(sum(row) for row in grid)

    if filled_buckets <= capacity:
        return filled_buckets // capacity
    
    filled_buckets_ceil = math.ceil(filled_buckets / capacity)
    num_buckets = buckets * wells
    num_fills = (num_buckets - filled_buckets_ceil) // capacity + 1
    
    return num_fills
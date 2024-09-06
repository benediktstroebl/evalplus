import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)

    filled_buckets = sum(sum(row) for row in grid)

    if filled_buckets <= capacity:
        return filled_buckets // capacity
    
    filled_buckets_per_well = filled_buckets // wells
    buckets_needed_per_well = (filled_buckets_per_well + capacity - 1) // capacity
    
    return buckets_needed_per_well * wells
capacity = 1
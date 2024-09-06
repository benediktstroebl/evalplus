import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)
    filled_buckets = sum(sum(row) for row in grid)
    return max(filled_buckets, math.ceil(wells / capacity))
import math
def max_fill(grid, capacity) :
    filled_buckets = sum(sum(row) for row in grid)
    max_fill = math.ceil(filled_buckets / capacity)
    
    return max_fill
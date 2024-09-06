import math
import numpy as np
def max_fill(grid, capacity):
    filled_rows = 0
    filled_cols = 0
    filled_wells = 0

    # Transforming the input list into a NumPy array for easier manipulation
    grid = np.array(grid).reshape(len(grid), -1)
    
    for row in grid:
        filled_rows += row.count(1)
        filled_cols += max(row)
        
        filled_wells += filled_rows * len(row)
    
    return max_wells_from_buckets(filled_wells, capacity)
def max_wells_from_buckets(filled_wells, capacity):
    return math.ceil(filled_wells / capacity)
capacity = 1
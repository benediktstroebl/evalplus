import math
import numpy as np
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.
    """
    # Calculate the maximum number of wells that can be filled
    well_width = len(grid)
    max_wells = math.ceil(capacity / well_width)
    
    filled_wells = 0
    
    # Iterate through each well to determine filled wells
    for well_row in grid:
        well_capacity = sum(well_row)
        filled_wells += max(0, int(well_capacity / capacity))
        
        if filled_wells >= max_wells:
            return max_wells - filled_wells
    
    return max_wells - filled_wells
capacity = 1
import math
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.
    """
    # Calculate the maximum number of wells that can be emptied with a single bucket
    well_width = len(grid)
    max_wells_per_bucket = math.ceil(well_width / capacity)
    
    # Calculate the total number of wells
    total_wells = sum(well_width for well in grid)
    
    # Calculate the total number of bucket lowers needed
    return total_wells // max_wells_per_bucket
capacity = 1
import math
def max_fill(grid, capacity):
    """
    Use buckets to empty wells efficiently.
    
    Parameters:
        - grid (2D list): Each row represents a well. 
        - capacity (int): Bucket capacity.
    
    Returns:
        - int: Number of times you need to lower the bucket.
    """
    # Calculate the dimensions of the grid
    num_wells = len(grid)
    num_rows_per_well = len(grid[0])
    
    # Initialize a counter for filled buckets
    filled_buckets = 0
    
    # Iterate through each well in the grid
    for well_index in range(num_wells):
        current_well = grid[well_index]
        
        # Initialize a counter for the current well
        well_filled_buckets = 0
        
        # Iterate through each row in the current well
        for row_index in range(num_rows_per_well):
            row = current_well[row_index]
            bucket_needed = math.ceil(len(row) / capacity)
            well_filled_buckets += bucket_needed
            
            # Add the max number of rows this bucket can fill
            filled_buckets += max(0, bucket_needed - 1)
        
        # Add the extra bucket needed to completely empty the well
        filled_buckets += well_filled_buckets
    
    return filled_buckets
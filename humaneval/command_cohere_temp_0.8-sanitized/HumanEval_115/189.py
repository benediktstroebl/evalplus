import math
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Parameters:
        grid (list of list): a rectangular grid of wells
        capacity (int): the capacity of each bucket

    Returns:
        int: the number of times you need to lower the bucket to empty the wells
    """
    # Calculate the lengths of the grid
    M = len(grid)
    N = len(grid[0])
    
    # Initialize variables
    count = 0
    bucket_full = False
    
    # Iterate through each cell in the grid
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                # Determine whether the bucket can be lowered
                if not bucket_full:
                    count += 1
                bucket_full = not bucket_full
            else:
                # The cell is empty, so the bucket can be raised
                bucket_full = False
    
    # If the final position of the bucket is filled, it needs to be raised again
    if bucket_full:
        count += 1
    
    # Return the final count
    return count
capacity = 1

def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Initialize variables
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_buckets = (num_rows + 1) // 2
    num_wells = num_rows * num_cols
    # Number of buckets needed
    buckets_needed = num_wells // capacity
    # Number of buckets available
    buckets_available = num_buckets
    # Number of times we need to lower the buckets
    num_lifted = 0

    # Check if we have enough buckets for the task
    if buckets_needed > buckets_available:
        return -1

    # Find the index of the start of each row
    row_indexes = []
    for i in range(num_rows + 1):
        if i % 2 == 0:
            row_indexes.append(i)

    # Find the index of the start of each column
    col_indexes = []
    for i in range(num_cols + 1):
        if i % 2 == 0:
            col_indexes.append(i)

    # Convert the 2d grid to 1d array
    arr = []
    for i in range(num_rows):
        for j in range(num_cols):
            arr.append(grid[i][j])

    # Iterate through the array and find the indices of water
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            # Get the index of the well
            well_i = row_indexes[i // num_cols]
            well_j = col_indexes[i % num_cols]
            # Get the number of water units in the well
            water = grid[well_i][well_j]
            # Iterate through the bucket and find the start index
            bucket_index = 0
            while water > 0:
                # Get the index of the bucket
                bucket_i = well_i + bucket_index
                bucket_j = well_j
                # Get the number of water units in the bucket
                water_in_bucket

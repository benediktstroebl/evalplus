
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
    rows, cols = grid.shape
    # Create a list to store the maximum number of wells that can be filled in each row
    max_wells = [[0] * cols for _ in range(rows)]
    # Create a list to store the number of buckets used to empty each row
    bucket_uses = [[0] * cols for _ in range(rows)]
    # Create a list to store the number of buckets used to empty each column
    bucket_column_uses = [[0] * rows for _ in range(cols)]
    # Loop over each row
    for row in range(rows):
        # Loop over each column in the current row
        for col in range(cols):
            # If the current well is empty, fill it
            if grid[row][col] == 0:
                # If the current well has already been filled, exit the loop
                if max_wells[row][col] == 1:
                    break
                # Fill the current well with the current bucket
                max_wells[row][col] = min(max_wells[row][col], 1)
                # Update the number of buckets used to empty the current row
                bucket_column_uses[col][row] = bucket_column_uses[col][row] + 1
                # Update the number of buckets used to empty the current column
                bucket_uses[row][col] = bucket_uses[row][col] + 1
    # Output the number of buckets used to empty each row and column
    for row in range(rows):
        print(bucket_column_uses[row][:])
    for col in range(cols):
        print(bucket_column_uses[:, col])
    # Output the maximum number of wells that can be filled in each row
    for row in range(rows):
        print(max_wells[row][:])

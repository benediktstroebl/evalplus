
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
    nb_rows = len(grid)
    nb_cols = len(grid[0])
    # List that counts the number of 1s in each column
    # 1 if there is a 1, 0 otherwise
    nb_ones = [0] * nb_cols
    # List that counts the number of 1s in each row
    # 1 if there is a 1, 0 otherwise
    nb_zeros = [0] * nb_rows

    # Compute nb_ones and nb_zeros
    for i in range(nb_rows):
        for j in range(nb_cols):
            if grid[i][j] == 1:
                nb_ones[j] += 1
            else:
                nb_zeros[i] += 1
    
    # Number of times we need to lower the bucket to fill the wells
    nb_times = 0
    # Number of times we need to lower the bucket to fill the wells that have 1s in the row
    nb_times_row = 0
    # Number of times we need to lower the bucket to fill the wells that have 1s in the col
    nb_times_col = 0
    # Count the number of times the bucket was lowered to fill the wells
    # We don't need to go through all the rows or columns, we just need to 
    # go through the ones that have the most 1s
    while nb_times_row <= nb_times_col:
        if nb_times_row < nb_times_col:
            # Get the index of the column with the most 1s
            # We start with the ones that have the most 1s
            max_ones_col = max(nb_ones)
            # Find the index of the column with the most 1s
            col_idx = nb_ones.index(max_ones_col)
            # If we can fill the column entirely with the capacity of the bucket
            if max_ones_col <= capacity:
                # Lower the bucket to fill the column
                nb_times_col += math.ceil(max_

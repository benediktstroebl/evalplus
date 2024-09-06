
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
    if not grid:
        return 0

    # Find the maximum value in the grid
    max_val = grid[0][0]
    for row in grid:
        max_val = max(max_val, row[0])

    # If the maximum value is 0, then all wells are empty and there are no drops needed
    if max_val == 0:
        return 0

    # Find the number of rows in the grid
    nrows = grid.shape[0]

    # Keep track of the number of drops needed
    drop_count = 0

    # Loop over all rows
    for i in range(nrows):
        # Find the indices of the rows with a 1 in the current row
        if grid[i][0] == 1:
            row_indices = [i]
        else:
            # If there is no 1 in the current row, try the rows above it
            row_indices = [i] + [j for j in range(i-1, nrows-1) if grid[j][0] == 1]

        # If there are no indices with a 1 in the current row, there are no drops needed
        if not row_indices:
            continue

        # Otherwise, use the buckets to empty the wells in the current row
        drop_count += min(max(capacity * row_indices, 0), 1) - 1

    return drop_count
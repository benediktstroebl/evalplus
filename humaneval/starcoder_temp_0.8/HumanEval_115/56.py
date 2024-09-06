
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
    # check whether there is a zero row or column in the grid
    zero_row = next((True for row in grid if 0 in row), False)
    zero_col = next((True for row in zip(*grid) if 0 in row), False)

    if zero_row or zero_col:
        # if zero row/column exists, fill zero row/column with 1 and fill rest with 0
        if zero_row:
            # fill zero row with 1
            for i in range(len(grid[0])):
                grid[0][i] = 1
            # fill rest of the grid with 0
            for i in range(1, len(grid)):
                grid[i][:] = [0 for _ in range(len(grid[i]))]
        if zero_col:
            # fill zero column with 1
            for i in range(len(grid)):
                grid[i][0] = 1
            # fill rest of the grid with 0
            for i in range(1, len(grid[0])):
                for j in range(len(grid)):
                    grid[j][i] = 0

    return max_fill_recursive(grid, capacity, 0, 0)


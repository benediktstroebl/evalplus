
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

    # define the height of the grid
    n = grid.length

    # initialize the number of times buckets need to be lowered
    count = 0

    # check the last row
    if (n-1) > 0:
        # check if the last cell is 1
        if grid[n-1][0] == 1:
            # check if the cell to the left is empty
            if grid[n-2][0] == 0:
                # check if the cell above is empty
                if grid[n-1][1] == 0:
                    # check if the cell to the right is empty
                    if grid[n][0] == 0:
                        # if all conditions are met, lower the bucket
                        grid[n][0] = 0
                        count += 1
                        
    # check the last column
    for i in range(1, n-1):
        # check if the cell is 1
        if grid[i][n-1] == 1:
            # check if the cell to the left is empty
            if grid[i-1][n-1] == 0:
                # check if the cell above is empty
                if grid[i][n-2] == 0:
                    # check if the cell to the right is empty
                    if grid[i+1][n-1] == 0:
                        # if all conditions are met, lower the bucket
                        grid[i][n-1] = 0
                        count += 1

    # check the last row and column
    for i in range(1, n-1):
        for j in range(1, n-1):
            # check if the cell is 1
            if grid[i][j] == 1:
                # check if the cell to the left is empty
                if grid[i-1][j] == 0:
                    # check if the cell above is empty
                    if grid[i][j-1] == 0:
                        # check if the cell to the right is empty
                        if grid[i+1][j] == 0:
                            # if all conditions are

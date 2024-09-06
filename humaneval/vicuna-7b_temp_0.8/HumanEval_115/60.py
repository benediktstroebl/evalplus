
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
    # initialize the number of times we need to lower the buckets
    times = 0
    # loop through each row of the grid
    for i in range(len(grid)):
        # loop through each well in the row
        for j in range(grid[i].length):
            # loop through each bucket
            for k in range(grid.length):
                # check if we can empty the well using the current bucket
                if grid[i][j] == 1:
                    # if we can, decrease the number of times we need to lower the buckets
                    times += 1
                    # empty the well using the current bucket
                    grid[i][j] = 0
    return times
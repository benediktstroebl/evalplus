
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
    # check if it's possible to fill the grid with 1's
    if not grid.fillable():
        return 0
    # loop through each row in the grid
    for row in grid:
        # loop through each well in the row
        for i in range(len(row)):
            # check if the well can be filled
            if not row[i]:
                # if the well can be filled, fill it and continue to the next well
                grid[i][j] = 1
                bucket_filled = 1
                j = j + 1
                continue
            # if the well can't be filled, move on to the next well
            bucket_filled = 0
        # check if all wells in the row have been filled
        if not bucket_filled:
            return j
    # if the grid is full, return the number of rows in the grid
    return grid.length
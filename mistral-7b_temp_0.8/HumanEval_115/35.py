
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
    ROWS, COLS = len(grid), len(grid[0])
    buckets = capacity
    # keep track of number of times we need to refill the bucket.
    # we could also just keep track of the number of empty wells left.
    times = 0
    # while the buckets are not empty, refill
    while buckets > 0:
        # keep track of number of wells that we fill
        filled = 0
        # start from the left most well
        for i in range(ROWS):
            # if we have empty wells,
            if grid[i][0] == 1:
                # fill the first well
                filled += 1
                # update the grid with the number of units of water we removed
                grid[i][0] -= 1
                # if we do not have any water left in the bucket
                if buckets == 0:
                    # we need to stop and refill the bucket
                    break
            # if we have empty wells,
            if grid[i][-1] == 1:

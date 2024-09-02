
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

    # init
    rows = len(grid)
    cols = len(grid[0])
    full = 0
    rows_done = [False for i in range(rows)]
    cols_done = [False for i in range(cols)]

    # get max
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                full += 1
    bucket = int(math.ceil(full / capacity))

    # fill the buckets
    for b in range(bucket):

        # increase bucket capacity
        full = 0
        for i in range(rows):
            for j in range(cols):
                if not rows_done[i] and not cols_done[j]:
                    full += 1
                    if full == capacity:
                        rows_done[i] = True
                        cols_done[j] = True
        bucket += int(math.ceil(full / capacity))
    
    # return the max
    return bucket


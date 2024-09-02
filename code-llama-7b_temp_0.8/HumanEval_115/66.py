
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
    if grid == None or len(grid) == 0:
        return 0

    water = 0
    rows, cols = len(grid), len(grid[0])
    if cols == 0:
        return 0

    # when moving up, it is equal to 
    # number of 1's to the left of it + 1
    left_1 = [0] * rows
    # when moving down, it is equal to 
    # number of 1's to the right of it + 1
    right_1 = [0] * rows
    # the highest number of water we can get from a well
    # this is used to compute the number of drops
    drops = [0] * rows

    for i in range(rows):
        # sum all the 1's in the row
        for j in range(cols):
            if grid[i][j] == 1:
                left_1[i] += 1
        # sum all the 1's in the row
        for j in range(cols - 1, -1, -1):
            if grid[i][j] == 1:
                right_1[i] += 1
        # compute the highest number of water we can get
        drops[i] = min(left_1[i], right_1[i])

    # compute the number of water we can get
    # from the highest number of water we can get
    # using the capacity of the buckets
    total_water = 0
    for i in range(rows):
        total_water += min(capacity, drops[i])
    
    # compute the number of times we need to 
    # lower the bucket
    return math.ceil(total_water / capacity)



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

    if not grid or len(grid) == 0:
        return 0

    # max amount of water in any well
    max_cap = 0
    for row in grid:
        max_cap += max(row)

    # number of rows
    row_num = len(grid)

    # number of columns
    col_num = len(grid[0])

    # if there's no capacity to fill, no need to fill
    if max_cap <= capacity:
        return 0

    # if all the wells are full, no need to fill
    if all([all(row) for row in grid]):
        return 0

    # the total number of units of water
    tot_unit = 0
    for row in grid:
        tot_unit += sum(row)

    # upper bound
    up_bound = min(tot_unit, max_cap)

    # lower bound
    low_bound = 1

    # find the number of lower buckets required
    num_bucket = math.ceil((up_bound + capacity - 1) / capacity)
    # print(num_bucket)

    # binary search
    while up_bound - low_bound > 1:
        mid = (low_bound + up_bound) // 2
        if max_fill_helper(grid, capacity, num_bucket, mid):
            up_bound = mid
        else:
            low_bound = mid
    return up_bound


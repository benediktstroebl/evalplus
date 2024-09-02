
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

    # brute force
    # for i, row in enumerate(grid):
    #     for j, val in enumerate(row):
    #         if val == 0:
    #             continue
    #         else:
    #             print('val', val)
    #             return math.ceil(val / capacity)

    # better solution
    # find number of rows that is less than capacity
    # return the number of rows

    # find number of rows
    total = 0
    for row in grid:
        # check if row is less than capacity
        total += row.count(0)

    # if total is less than capacity then return 0
    if total < capacity:
        return 0

    # else return the number of rows
    return math.ceil(total / capacity)


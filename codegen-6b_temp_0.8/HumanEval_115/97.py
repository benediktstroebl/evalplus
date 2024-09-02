
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
    # the grid is of them, rows first, column from the right, so always take the max of the rows
    # if the previous elem is 0, do nothing, if the previous elem is 1, 
    # we start to check the capacity of the bucket
    # if the bucket is not enough, we need to go back to the previous row, if the bucket is not enough, 
    # we move to the next column and repeat the process until we find the last elem
    # then we add 1 to the result

    row, col = len(grid), len(grid[0])
    result = 0
    for i in range(row):
        capacity_cum = 0
        for j in range(col-1, -1, -1):
            if grid[i][j] == 1:
                capacity_cum += capacity
            elif capacity_cum != 0:
                capacity_cum = 0
                result += 1
    return result

import math
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells, 
    and each well has a bucket that can be used to extract water from it.

    Your task is to use the buckets to empty the wells. 
    Output: number of times you need to lower the buckets.

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
       
        * 1 <= grid[i][j].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    wells = [0]*(len(grid)//2)
    buckets = [0]*(len(grid)//2)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                wells[i][j//2] = 1
                buckets[i][j//2] = capacity
    return sum(wells) + sum(buckets)
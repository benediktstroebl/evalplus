
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

    bucket_capacity = capacity
    grid = grid
    bucket_number = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                bucket_number += 1
    
    filled = 0
    row = 0
    column = 0
    while bucket_number > 0:
        column += 1
        if column >= len(grid[0]):
            row += 1
            column = 0
        if row >= len(grid):
            break
        if grid[row][column] == 1:
            filled += 1
            grid[row][column] = 0
            bucket_number -= 1
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                bucket_number += 1
    
    return math.ceil(bucket_number/bucket_capacity)


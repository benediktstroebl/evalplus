
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

    rows = len(grid)
    columns = len(grid[0])
    left = [0 for _ in range(columns)]
    right = [0 for _ in range(columns)]
    bottoms = [0 for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                left[column] = max(left[column], row)
                right[column] = max(right[column], rows - row - 1)
                bottoms[row] = max(bottoms[row], column)
            else:
                left[column] = 0
                right[column] = 0
                bottoms[row] = 0
    
    max_water = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                max_water = max(max_water, min(left[column], row) + min(right[column], rows - row - 1) - 1)
    
    for row in range(

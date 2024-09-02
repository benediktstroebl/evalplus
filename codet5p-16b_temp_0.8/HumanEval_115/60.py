
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

    if len(grid) == 0 or len(grid[0]) == 0 or capacity == 0:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    bucket_capacity = capacity
    max_fill_count = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                bucket_capacity = bucket_capacity - 1
                max_fill_count = max_fill_count + 1
                left_to_fill = (rows-1) - i
                left_to_fill = left_to_fill + 1
                right_to_fill = (columns-1) - j
                right_to_fill = right_to_fill + 1
                left_max_fill_count = math.floor(bucket_capacity / left_to_fill)
                right_max_fill_count = math.floor(bucket_capacity / right_to_fill)
                max_fill_count = max(max_fill_count, left_max_fill_count, right

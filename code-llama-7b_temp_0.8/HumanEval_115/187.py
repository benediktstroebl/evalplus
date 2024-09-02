
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
    if grid == None or len(grid) == 0 or capacity == 0:
        return 0

    max_fill_count = 0
    bucket_count = 0
    bucket_capacity = capacity
    row_count = len(grid)
    column_count = len(grid[0])
    bucket_limit = 10
    for row in grid:
        if bucket_limit < bucket_count:
            bucket_limit += 1
            bucket_capacity += capacity
        
        bucket_count = 0
        for cell in row:
            if cell == 1:
                bucket_count += 1
            elif bucket_count > 0:
                bucket_count -= 1
            else:
                bucket_count += capacity
                if bucket_count < 0:
                    bucket_count = 0
                    break

            if bucket_count == bucket_capacity:
                bucket_count = 0
                max_fill_count += 1

    return max_fill_count



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

    def buckets_used(grid, capacity):
        count = 0
        for row in grid:
            for bucket in row:
                if bucket == 1:
                    count += 1
        return count
    
    row_count = len(grid)
    col_count = len(grid[0])

    for row in grid:
        if len(row)!= col_count:
            return -1

    water = 0
    for row in grid:
        for bucket in row:
            if bucket == 1:
                water += 1

    if capacity < water:
        return -1

    row_count = len(grid)
    col_count = len(grid[0])

    max_filled = 0
    for i in range(row_count):
        for j in range(col_count):
            grid[i][j] = 0

            while buckets_used(grid, capacity) > 0:
                max_filled += 1

                for row in grid:
                    row[:] = sorted(row, reverse = True)

                for row in grid:
                    for i in range(col_count

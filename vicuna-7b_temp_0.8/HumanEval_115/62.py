
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

    rows, cols = grid.shape
    max_bucket_index = max(grid)
    bucket_capacity = max_bucket_index * bucket_capacity
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if grid[row][col + 1] != 1 and grid[row][col + 1] != max_bucket_index:
                    grid[row][col] = 0
                    grid[row][col + 1] = max_bucket_index
                    for i in range(max_bucket_index):
                        if (grid[row][col] == 1 and grid[row+i][col] == 0) or (grid[row+i][col] == 1 and grid[row][col] == 0):
                            grid[row+i][col] = 0
                            bucket_index = 0
                            while grid[row+i][col] == 1:
                                bucket_index = bucket_index + 1
                                grid[row+i][col] = 0
                            grid[row+i][col] = bucket_index
                    return max_bucket_index
                elif grid[row][col + 1] == max_bucket_index:
                    grid[row][col] = 0
                    grid[row+1][col] = max_bucket_index
                    for i in range(max_bucket_index):
                        if grid[row][col] == 1 and grid[row+i][col] == 0 or grid[row+i][col] == 1 and grid[row+i][col + 1] == 1:
                            grid[row+i][col] = 0
                            bucket_index = 0
                            while grid[row+i][col] == 1:
                                bucket_index = bucket_index + 1
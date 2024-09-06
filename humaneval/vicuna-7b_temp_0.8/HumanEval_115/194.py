
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
    def dfs(grid, i, j):
        if grid[i][j] == 0:
            return 0
        if grid[i][j] == 1:
            return 1
        if grid[i][j] == 2:
            return 2
        if grid[i][j] == 3:
            return 3
        if grid[i][j] == 4:
            return 4
        if grid[i][j] == 5:
            return 5
        if grid[i][j] == 6:
            return 6
        if grid[i][j] == 7:
            return 7
        if grid[i][j] == 8:
            return 8
        if grid[i][j] == 9:
            return 9
        return 0

    bucket_count = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == 0:
                bucket_count = max(bucket_count, dfs(grid, i, 0))
            if row[i] == 1:
                bucket_count = max(bucket_count, dfs(grid, i, 1))
    return bucket_count

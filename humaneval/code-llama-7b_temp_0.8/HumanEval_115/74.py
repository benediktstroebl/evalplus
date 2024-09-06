
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
    def helper(i, j, buckets):
        if i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return False
        if buckets < 0:
            return False
        if grid[i][j] == 1:
            grid[i][j] = 0
            return True
        if grid[i][j] == 0:
            return False

        r = helper(i, j-1, buckets-1)
        d = helper(i+1, j, buckets)
        l = helper(i, j+1, buckets)
        u = helper(i-1, j, buckets)

        return (r or d or l or u)


    def dfs(i, j, buckets):
        if i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return False
        if buckets < 0:
            return False
        if grid[i][j] == 1:
            grid[i][j] = 0
            return True
        if grid[i][j] == 0:
            return False

        r = dfs(i, j-1, buckets-1)
        d = dfs(i+1, j, buckets)
        l = dfs(i, j+1, buckets)
        u = dfs(i-1, j, buckets)

        return (r or d or l or u)

    def is_pos_fair(i, j):
        return (i >= 0 and i < len(grid) and 
                j >= 0 and j < len(grid[i]) and 
                grid[i][j] == 1)

    # result = helper(0, 0, capacity)
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if grid[i][j] == 1:
            result += 1
            dfs(i, j, capacity-1)
            # print(grid)

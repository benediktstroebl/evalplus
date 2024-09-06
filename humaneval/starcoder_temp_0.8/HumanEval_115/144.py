
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
    """
    Approach 1:
        * Build a dp table of the size of grid
            * dp[i][j] -> min number of operations to move water from grid[i][j] to it's neighbour
    """
    def dfs(grid, capacity, i, j, depth):
        if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]) or grid[i][j] == 0:
            return math.inf
        
        if depth > capacity:
            return math.inf
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return depth
        
        grid[i][j] = 0
        depth += 1
        return min(
            dfs(grid, capacity, i + 1, j, depth),
            dfs(grid, capacity, i - 1, j, depth),
            dfs(grid, capacity, i, j + 1, depth),
            dfs(grid, capacity, i, j - 1, depth),
        )

    return dfs(grid, capacity, 0, 0, 0)


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
    m, n = len(grid), len(grid[0])
    def dfs(grid, i, j, cap, vis):
        if i < 0 or i >= m or j < 0 or j >= n: return 0
        if cap == 0: return 0
        if grid[i][j] == 0: return 0
        if (i, j) in vis: return 0
        vis.add((i, j))
        if grid[i][j] == 1:
            return 1 + max(dfs(grid, i+1, j, cap, vis), dfs(grid, i-1, j, cap, vis), dfs(grid, i, j+1, cap, vis), dfs(grid, i, j-1, cap, vis))
        return 0

    count = 0
    vis = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count += math.ceil(dfs(grid, i, j, capacity, vis) / capacity)

    return count

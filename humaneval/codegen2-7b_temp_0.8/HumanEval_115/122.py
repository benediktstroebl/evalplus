
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
    n_rows = len(grid)
    n_cols = len(grid[0])
    visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
    print(grid)
    res = 0
    def dfs(i, j):
        if i < 0 or i > n_rows-1 or j < 0 or j > n_cols-1 or visited[i][j]: return
        visited[i][j] = True
        if grid[i][j] == 0:
            res += 1
        else:
            for x,y in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                dfs(x,y)
    dfs(0,0)
    return res

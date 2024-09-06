
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
    N, M = len(grid), len(grid[0])
    visited = [[False for _ in range(M)] for _ in range(N)]

    def dfs(r, c, depth, t):
        if (r, c) in visited or depth == capacity or grid[r][c] == 0:
            return 0
        visited[r][c] = True
        total_water = 0
        for nr, nc in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
            if 0 <= nr < N and 0 <= nc < M:
                total_water += dfs(nr, nc, depth+1, t)
        total_water += depth * grid[r][c]
        visited[r][c] = False
        return total_water

    t = 0
    for r in range(N):
        for c in range(M):
            t += dfs(r, c, 0, t)
    return t



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
    # DFS
    visited = [[False] * n for _ in range(m)]
    path = [[[0] * 4 for _ in range(n)] for _ in range(m)]
    level = 0
    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n) or grid[i][j] or visited[i][j]:
            return 0
        if capacity == 0:
            return math.inf
        visited[i][j] = True
        for x, y in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
            if dfs(x, y) < math.inf:
                path[i][j][0] = x
                path[i][j][1] = y
                path[i][j][2] = x - i
                path[i][j][3] = y - j
                return 1
        return 0
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] or visited[i][j]:
                continue
            ans += dfs(i, j)
    return ans

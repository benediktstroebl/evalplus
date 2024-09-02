
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
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[j][i] = dp[j-1][i] + dp[j][i-1] - dp[j-1][i-1] + grid[i-1][j-1]
    def dfs(i, j, capacity):
        if dp[j][i] > capacity:
            return float('inf')
        if i == 0 and j == 0:
            return 0
        if i == 0:
            return dfs(i, j-1, capacity)
        if j == 0:
            return dfs(i-1, j, capacity)
        return min(dfs(i, j-1, capacity) + 1,
                dfs(i-1, j, capacity) + 1)
    return dfs(m, n, capacity)

def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    start = [i for i in range(n)]
    for i in range(1, k + 1):
        for j in range(n):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0)]:
                nei_val = grid[nei[0]][nei[1]] if 0 <= nei[0] < n and 0 <= nei[1] < n else float('inf')
                if nei_val != float('inf') and dp[i - 1][nei_val] + 1 < dp[i][j]:
                    dp[i][j] = dp[i - 1][nei_val] + 1
                    start[j] = nei_val
    
    result = [start[j] for j in range(n) if dp[k][j] == k]
    return result
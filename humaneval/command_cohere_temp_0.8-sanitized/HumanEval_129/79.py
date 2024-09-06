def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    edges = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(1, k + 1):
        for j in range(n):
            for dx, dy in edges:
                x, y = j + dx, i + dy
                if 0 <= x < n and 0 <= y < i and grid[x][y] < dp[i][j]:
                    dp[i][j] = grid[x][y]
    ans = []
    for j in range(n):
        for i in range(k, 0, -1):
            if dp[i][j] != float('inf'):
                ans.append(dp[i][j])
                break
    return ans
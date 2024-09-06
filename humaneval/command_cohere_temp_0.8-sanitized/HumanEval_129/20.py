def minPath(grid, k):
    n = len(grid)
    dp = [float('inf')] * n * n
    st = [None] * n * n
    res = []
    def dfs(i, j, c):
        if c == k:
            nonlocal res
            res.extend(st[i] for i in range(j, i+k+1))
            return
        if dp[i][j] != float('inf'):
            return
        dp[i][j] = 0
        dfs(i, j, c+1)
        for nei in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] != c:
                dfs(nei[0], nei[1], c+1)

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                st[i * n + j] = grid[i][j]
                dfs(i, j, 1)
    return res
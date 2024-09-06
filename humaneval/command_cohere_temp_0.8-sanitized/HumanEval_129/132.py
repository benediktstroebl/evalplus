def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    vis = [False] * (n * n)
    res = []
    
    # Initialization
    for i in range(n):
        dp[0][i] = grid[i][0]
    
    # Finding minimum values
    for len_path in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if not vis[i * n + j] and grid[i][j] < dp[len_path][i]:
                    dp[len_path][i] = grid[i][j]
                    res.append(grid[i][j])
                    vis[i * n + j] = True
                    nei = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for x, y in nei:
                        if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y] < dp[len_path][i + x]:
                            dp[len_path][i + x] = grid[i + x][j + y]
                            res.append(grid[i + x][j + y])
                            vis[i * n + j] = vis[i + x * n + j + y] = True
    
    # Returning minimum path
    lst = [0] * k
    i = n - 1
    j = n - 1
    while len(lst) < k:
        lst.append(dp[k][i] * n + dp[k][j])
        i, j = (i - 1, j - 1)
        if i < 0:
            i = n - 1
        if j < 0:
            j = n - 1
    lst.reverse()
    return lst
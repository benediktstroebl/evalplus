def minPath(grid, k):
    n = len(grid)
    dp = [float('inf')] * n * n
    dist = [float('inf')] * n * n
    
    def dfs(i, j, k):
        if k == 0:
            return grid[i][j]
        if dp[i][j] != float('inf'):
            return dp[i][j]
        minVal = float('inf')
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            tmp = dfs(ni, nj, k-1)
            if tmp < minVal:
                minVal = tmp
        dp[i][j] = minVal
        return minVal
    
    for i in range(n):
        for j in range(n):
            dist[i * n + j] = dfs(i, j, k)
    
    minPath = []
    i, j = n-1, n-1
    while i >= 0 and j >= 0:
        if dist[i * n + j] == float('inf'):
            i -= 1
            j -= 1
        else:
            minPath.append(dist[i * n + j])
            i -= 1
            j -= 1
    
    minPath.reverse()
    return minPath
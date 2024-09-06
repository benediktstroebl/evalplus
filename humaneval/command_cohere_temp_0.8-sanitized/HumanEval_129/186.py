def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return dp[r][c]
        visited[r, c] = True

        # try going upwards
        if 0 < r and grid[r-1][c] < grid[r][c] and dfs(r-1, c, path+(grid[r-1][c]), visited, dp):
            return dp[r][c]

        # try going downwards
        if r < N-1 and grid[r+1][c] < grid[r][c] and dfs(r+1, c, path+(grid[r+1][c]), visited, dp):
            return dp[r][c]

        # try going leftwards
        if 0 < c and grid[r][c-1] < grid[r][c] and dfs(r, c-1, path+(grid[r][c-1]), visited, dp):
            return dp[r][c]

        # try going rightwards
        if c < N-1 and grid[r][c+1] < grid[r][c] and dfs(r, c+1, path+(grid[r][c+1]), visited, dp):
            return dp[r][c]

        # no better path found, this is the answer
        dp[r][c] = path
        return path

    if k > N*N or k <= 0:
        return []

    path = []
    visited = [False] * N * N
    dp = [[] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r, c]:
                path = dfs(r, c, path, visited, dp)

    # Since the path is constructed in reverse order, we need to reverse it again to get the correct order
    return path[::-1]
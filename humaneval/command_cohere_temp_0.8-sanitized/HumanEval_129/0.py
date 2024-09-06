def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True
        if (r, c) in visited:
            return False
        visited[r, c] = True

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and dfs(nr, nc, path+[grid[nr][nc]], visited, dp):
                return True
        
        # Store the candidate path
        dp[r][c] = True
        
        return False

    visited = [[False for _ in range(N)] for _ in range(N)]
    dp = [[False for _ in range(N)] for _ in range(N)]
    path = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and not dfs(i, j, path, visited, dp):
                return []

    return path[::-1]
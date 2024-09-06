def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True
        if (r, c) in visited:
            return False
        visited[(r, c)] = True

        # Check all 4 directions
        if dfs(r-1, c, path + [grid[r-1][c]], visited, dp) or \
           dfs(r+1, c, path + [grid[r+1][c]], visited, dp) or \
           dfs(r, c-1, path + [grid[r][c-1]], visited, dp) or \
           dfs(r, c+1, path + [grid[r][c+1]], visited, dp):
            dp[r][c] = 1
            return True

        return False

    if k > N*N or k < 1:
        return []

    dp = [[0 for _ in range(N)] for _ in range(N)]
    visited = {}
    minPath = []

    for r in range(N):
        for c in range(N):
            if not dfs(r, c, [], visited, dp):
                continue
            minPath = [grid[r][c]] + minPath
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < N and 0 <= nc < N and dp[nr][nc] == 1:
                    minPath = [grid[nr][nc]] + minPath

    return minPath
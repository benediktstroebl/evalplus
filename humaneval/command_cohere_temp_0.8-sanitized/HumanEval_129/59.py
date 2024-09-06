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
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == grid[r][c] and not visited[nr, nc]:
                dp[nr][nc] = 1
                if dfs(nr, nc, path, visited, dp):
                    return True
        return False

    if k == 1:
        return [grid[0][0]] if grid[0][0] < grid[1][1] else [grid[1][1]]
    if k == 2:
        return [grid[0][0], grid[1][0]] if grid[0][0] < grid[1][0] else [grid[0][1], grid[1][1]]

    visited = [[False] * N for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    return [grid[r][c] for r, c in reversed(list(dfs(0, 0, [], visited, dp))) if len(path) == k]
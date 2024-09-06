def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return None
        visited[r, c] = True

        # Explore all possible paths from this cell
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0 and (nr, nc) not in visited:
                neigPath = dfs(nr, nc, path + [grid[nr][nc]], visited, dp)
                if neigPath is not None:
                    if neigPath not in dp:
                        dp[neigPath] = 1
                    else:
                        dp[neigPath] += 1
                    if len(neigPath) == k:
                        return neigPath
        
        return None

    dp = {}
    visited = [[False] * N for _ in range(N)]
    path = dfs(0, 0, [], visited, dp)
    return path[1:] if path else []
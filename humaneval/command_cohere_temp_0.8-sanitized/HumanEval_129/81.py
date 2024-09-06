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
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != path[-1] and dfs(nr, nc, path + [grid[nr][nc]], visited, dp):
                return True
                # Found a valid path, update the dp value if the found path has smaller len()
                if len(path) + 1 == k:
                    dp[r][c] = nr
                    return True

        return False

    if k == 1:
        return [grid[0][0]] if grid[0][0] != 0 else []

    dp = [[-1 for _ in range(N)] for _ in range(N)]
    visited = [False for _ in range(N)]
    # Start the DFS from the first row and column
    row, col = next((r, c) for r in range(N) for c in range(N) if not visited[r][c])
    path = [grid[row][col]]
    if not dfs(row, col, path, visited, dp):
        return []
    # Found the shortest path, now backtrack to get the answer
    res = [grid[r][c] for r, c in reversed(dp[row]) if grid[r][c] != 0]
    return res
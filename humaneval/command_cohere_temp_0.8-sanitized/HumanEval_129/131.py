def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, temp):
        if len(path) == k:
            return True if sorted(path) == path else False

        visited[r][c] = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc]:
                if dfs(nr, nc, path + [grid[nr][nc]], visited, temp):
                    return True
        return False

    visited = [[False] * N for _ in range(N)]
    temp = [0] * N
    minPath = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and dfs(r, c, [], visited, temp):
                minPath = sorted(minPath + [grid[r][c]])
                if len(minPath) == k:
                    return minPath
    return minPath
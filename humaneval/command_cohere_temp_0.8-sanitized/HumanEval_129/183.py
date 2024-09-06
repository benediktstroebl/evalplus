def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, counter):
        if len(path) == k:
            return True, path

        if counter == N * N:
            return False, path

        visited[r][c] = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc]:
                res, tmpPath = dfs(nr, nc, path + [grid[nr][nc]], visited, counter + 1)
                if res:
                    return res, tmpPath

        return False, path

    visited = [[False for _ in range(N)] for _ in range(N)]
    path = []
    return dfs(0, 0, path, visited, 1)[1]
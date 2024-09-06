def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, counter):
        if len(path) == k:
            return True
        if counter == k:
            return False
        visited[r][c] = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc]:
                if dfs(nr, nc, path + [grid[nr][nc]], visited, counter + 1):
                    return True
        return False
    
    visited = [[False] * N for _ in range(N)]
    path = []
    return [p for p in grid if not visited[p[0]][p[1]] and dfs(p[0], p[1], path, visited, 1)]
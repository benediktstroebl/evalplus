def minPath(grid, k):
    N = len(grid)
    visited = [False] * (N * N)
    def dfs(r, c, remaining):
        if remaining == 0:
            return grid[r][c]
        if visited[r * N + c]:
            return float('inf')

        visited[r * N + c] = True
        minVal = float('inf')
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and not visited[nr * N + nc] and grid[nr][nc] != grid[r][c]:
                minVal = min(minVal, grid[nr][nc] + dfs(nr, nc, remaining-1))
        return minVal

    return [dfs(r, c, k) for r, c in enumerate(range(N)) if not visited[r * N + c]]
def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    def dfs(r, c, remaining):
        if remaining == 0:
            return grid[r][c]
        if (r, c) in visited[r][c]:
            return float('inf')
        visited[r][c].add((r, c))
        minVal = float('inf')
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) != (r, c) and grid[nr][nc] != float('inf'):
                minVal = min(minVal, grid[nr][nc] + dfs(nr, nc, remaining-1))
        return minVal
    return dfs(0, 0, k)
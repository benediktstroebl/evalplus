def minPath(grid, k):
    N = len(grid)
    visited = [set() for _ in range(N)]
    def dfs(r, c, remaining):
        if remaining == 0:
            return grid[r][c]
        if (r, c) in visited[r]:
            return float('inf')
        visited[r].add((r, c))
        minVal = float('inf')
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != (r, c):
                minVal = min(minVal, grid[nr][nc] + dfs(nr, nc, remaining-1))
        return minVal
    return dfs(0, 0, k)
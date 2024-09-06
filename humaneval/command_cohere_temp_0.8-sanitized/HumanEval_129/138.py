def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, d):
        if d == k:
            ret.append(path)
            return 
        if visited[r][c]:
            return 
        visited[r][c] = True
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc]:
                dfs(nr, nc, path+[grid[nr][nc]], visited, d+1)
    ret = []
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                dfs(r, c, [grid[r][c]], visited, 1)
    # Remove duplicates and sort by increasing order
    seen = set()
    return [sorted(path) for path in ret if list(path) not in seen and not seen.add(list(path))]
def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, ds):
        if len(path) == k:
            return True
        if visited[r][c]:
            return False
        visited[r][c] = True
        path.append(grid[r-1][c-1])
        for dr, dc in [(0,1), (1,1), (1,0), (1,-1)]:  # four neighbors
            if 0 <= r+dr < N and 0 <= c+dc < N and grid[r+dr][c+dc] != 0 and not visited[r+dr][c+dc]:
                if dfs(r+dr, c+dc, path, visited, ds):
                    return True
                ds.append(path)
                path.pop()
                visited[r+dr][c+dc] = False
        return False
        
    ds = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] != 0 and not visited[r][c] and dfs(r, c, path, visited, ds):
                return path
    return ds
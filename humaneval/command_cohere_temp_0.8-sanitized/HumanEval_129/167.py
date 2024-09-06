def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, memo):
        if len(path) == k:
            return True
        if (r, c) in memo:
            return False
        memo[r, c] = True
        if r < 0 or c < 0 or r >= N or c >= N:
            return False
        if visited[r, c]:
            return False
        visited[r, c] = True
        path.append(grid[r][c])
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(r + dr, c + dc, path, visited, memo):
                return True
        return False
    path = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    memo = [False for _ in range(N * N)]
    for r in range(N):
        for c in range(N):
            if not dfs(r, c, path, visited, memo):
                continue
            path.pop()
            return path
    return []
def minPath(grid, k):
    N = len(grid)
    visited = [False] * N * N
    stack = []
    values = []
    def dfs(r, c, remaining):
        if remaining == 0:
            return True
        if visited[r * N + c]:
            return False
        visited[r * N + c] = True
        stack.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0 and not visited[nr * N + nc] and dfs(nr, nc, remaining - 1):
                return True
        return False
    while stack or len(values) < k:
        (r, c) = stack.pop() if stack else (0, 0)
        values.append(grid[r][c])
        if not dfs(r, c, k - len(values)):
            return None
    return values[::-1]
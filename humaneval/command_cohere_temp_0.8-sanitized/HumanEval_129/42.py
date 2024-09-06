def minPath(grid, k):
    N = len(grid)
    visited = [False] * N * N
    stack = []
    values = []
    def dfs(r, c):
        if visited[r * N + c]:
            return
        visited[r * N + c] = True
        values.append(grid[r][c])
        if k == 0:
            return
        stack.append((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr * N + nc] and grid[nr][nc] != values[-1]:
                dfs(nr, nc)
        while stack and k > 1 and grid[stack[-1][0]][stack[-1][1]] == values[-1]:
            k -= 1
            stack.pop()
        if k == 1:
            return
    for r in range(N):
        for c in range(N):
            if not visited[r * N + c]:
                dfs(r, c)
    return values
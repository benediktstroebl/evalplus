def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    dp = [float('inf')] * N * N
    dist = [float('inf')] * N * N

    def dfs(r, c, dist_so_far):
        if dist_so_far >= k:
            return True
        if dp[r * N + c] < dist_so_far:
            return False
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and dfs(nr, nc, dist_so_far + 1):
                dp[r * N + c] = dist_so_far
                return True
        return False

    for r in range(N):
        for c in range(N):
            if grid[r][c] != 0:
                dist[r * N + c] = 1
                dfs(r, c, 1)

    res = []
    for dr in range(N):
        for dc in range(N):
            if dist[dr * N + dc] == k:
                res.append(grid[dr][dc])
                if len(res) == k:
                    break

    return res
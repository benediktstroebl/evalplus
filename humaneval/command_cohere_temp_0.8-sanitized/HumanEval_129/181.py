def minPath(grid, k):
    n = len(grid)
    dp = [None] * (n * n)
    for i in range(n):
        for j in range(n):
            dp[i * n + j] = [grid[i][j], i, j]
    q = [(0, 0)]
    while len(q) > 0:
        x, y = q.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and dp[new_x * n + new_y] is not None:
                neighbor = dp[new_x * n + new_y]
                if neighbor[0] < dp[x * n + y][0]:
                    dp[x * n + y] = neighbor
                    q.append((x, y))
                if k == 1:
                    return [dp[x * n + y][0]]
            elif new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
                continue
            else:
                q.append((new_x, new_y))
    return []
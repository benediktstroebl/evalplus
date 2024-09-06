def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    dp[0][0] = 0
    stack = [([0, 0], [grid[0][0]])]
    while stack:
        weight, path = stack.pop()
        for i in range(N):
            for j in range(N):
                if i == 0 or j == 0:
                    continue
                if grid[i][j] < path[-1]:
                    continue
                if dp[weight][j] > dp[weight - 1][j - 1] + 1:
                    dp[weight + 1][j] = dp[weight - 1][j - 1] + 1
                    stack.append((weight + 1, path + [grid[i][j]]))
    return path[::-1][:k]
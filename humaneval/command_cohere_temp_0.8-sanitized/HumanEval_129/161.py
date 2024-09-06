def minPath(grid, k):
    N = len(grid)
    if k > N:
        return None

    dp = [None] * N
    dp[0] = [i for i in range(N)]

    for i in range(1, N):
        for j in range(N):
            if dp[i - 1][j] == k:
                continue
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0), (j, 2)]:
                nei_cell = nei[0]
                nei_dir = nei[1]
                if 0 <= nei_cell < N and nei_dir != 0 and (grid[i][nei_cell] != 0 or dp[i - 1][nei_cell] == k):
                    if dp[i - 1][nei_cell] == k:
                        continue
                    dp[i] = sorted(set(dp[i][:k]).union(set(dp[i - 1][nei_cell:k])))
                    break

    return dp[N - 1][:k]
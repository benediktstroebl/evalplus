def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(1, k+1):
        for j in range(N):
            for di in (-1, 0, 1):
                nei = (j + di) % N
                if (dp[i-1][nei] + 1 < dp[i][j] or
                        (dp[i-1][nei] + 1 == dp[i][j] and grid[j][nei] < grid[j][j])):
                    dp[i][j] = dp[i-1][nei] + 1
                    if dp[i][j] == 0:
                        dp[i][j] = float('inf')
    ans = []
    curr = dp[k][0]
    while curr != float('inf'):
        ans.append(curr)
        curr = dp[0][curr]
    return ans[::-1]
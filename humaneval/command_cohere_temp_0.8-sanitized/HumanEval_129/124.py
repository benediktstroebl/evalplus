def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(k+1):
        for j in range(N):
            for nei in [(j+1,0),(j-1,0),(0,j+1),(0,j-1)]:
                if nei[0] < N and nei[1] < N and grid[nei[0]][nei[1]] < dp[i][j]:
                    dp[i+1][nei[0]] = dp[i][j] + 1
                    dp[i+1][nei[1]] = dp[i][j] + 1
    ans = []
    i, j = k, N-1
    while i > 0 and j >= 0:
        if grid[j][i-1] < dp[i-1][j]:
            i -= 1
        else:
            ans.append(grid[j][i-1])
            j -= 1
            i -= 1
    if i > 0:
        for _ in range(i):
            ans.append(grid[N-1][i-1])
    return ans[::-1]
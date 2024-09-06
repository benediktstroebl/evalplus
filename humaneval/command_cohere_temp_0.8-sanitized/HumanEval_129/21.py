def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            for nei in [(j - 1, -1), (j, 0), (j + 1, 1)]:
                nei_row, nei_col = nei
                if nei_row < 0 or nei_col < 0 or nei_row >= n or nei_col >= n:
                    continue
                nei_value = grid[nei_row][nei_col]
                if nei_value == 0:
                    continue
                curr = 1 << (nei_value - 1)
                for l in range(i - 1):
                    dp[l][j] = min(dp[l][j], dp[l][nei_row] + curr)
                dp[i][j] = min(dp[i][j], dp[i - 1][nei_row] + curr)
    ans = []
    j = k
    while j > 0:
        ans.append(j)
        j = (j & (j - 1)) // -1  # Equivalent to xor trick
    return ans[::-1]  # Reverse the list as the problem asks for lexicographically smallest path
def minPath(grid, k):
    n = len(grid)
    dp = [float('inf')] * n * n
    stack = [(-1, -1)]  # (row, col)

    while stack:
        row, col = stack.pop()
        for nei in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] != k:
                dp[row * n + col] = min(dp[row * n + col], grid[nei[0]][nei[1]] + 1)
                stack.append(nei)

    ans = []
    for i in range(k):
        ans.append(dp[i])
    return ans
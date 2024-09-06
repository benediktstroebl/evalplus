def minPath(grid, k):
    n = len(grid)
    dp = [float('inf')] * n * n
    stack = [(0, 0)]  # (row, col)
    while stack:
        row, col = stack.pop()
        if dp[row * n + col] >= k:
            continue
        for nei in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] != 0 and dp[row * n + col] + 1 < dp[nei[0] * n + nei[1]]:
                dp[nei[0] * n + nei[1]] = dp[row * n + col] + 1
                stack.append(nei)
    ans = []
    i, j = 0, 0
    while i < n * n and j < k:
        for nei in [(i // n, j), (i // n, j + 1), (i // n + 1, j), (i // n - 1, j)]:
            if nei[0] == nei[0] and nei[1] == nei[1]:
                break
            if grid[nei[0]][nei[1]] != 0 and dp[nei[0] * n + nei[1]] == j:
                ans.append(grid[nei[0]][nei[1]])
                j += 1
                i = nei[0] * n + nei[1]
                break
        if j == k:
            break
    return ans
def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(k + 1):
        for j in range(n):
            for nei in [(j, left), (j, right), (left, j), (right, j)]:
                nei_val = grid[nei[0]][nei[1]]
                if nei_val != 0 and i + nei_val <= k:
                    dp[i + nei_val][nei[0]] = nei_val + dp[i][nei[0]]
                    dp[i + nei_val][nei[1]] = nei_val + dp[i][nei[1]]
    res = []
    curr = k
    for i in range(n):
        while curr > 0 and grid[i][curr - 1] == 0:
            curr -= 1
        if curr == 0:
            continue
        while curr > 0 and grid[i][curr - 1] != 0:
            res.append(grid[i][curr - 1])
            curr -= 1
    return res[::-1]
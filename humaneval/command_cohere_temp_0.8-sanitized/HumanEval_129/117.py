def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [i for i in range(N)]
    wall = [-1 for _ in range(N)]
    for i in range(k):
        for j in range(N):
            for nei in [(j - 1, -1), (j + 1, 1), (j, 0)]:
                if nei[0] >= 0 and nei[0] < N and nei[1] >= -1 and nei[1] <= 1 and grid[j][nei[0]] < dp[i][nei[0]]:
                    dp[i + 1][nei[0]] = grid[j][nei[0]]
                    start[nei[0]] = j
                    wall[nei[0]] = j
                    if i == k - 1:
                        break
    ans = []
    while k:
        temp = [start[i] for i in range(N) if dp[k][i] == dp[k - 1][i]]
        temp.sort()
        for j in temp:
            ans.append(grid[j][wall[j]])
        k -= 1
    return ans
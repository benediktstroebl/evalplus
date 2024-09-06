def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    starts = [(-1, -1) for _ in range(k + 1)]

    # Initialize the first column as the smallest valid path
    for i in range(N):
        dp[0][i] = grid[i][0]

    # Iterate through the rows to build the DP array
    for j in range(1, N):
        for i in range(1, k + 1):
            min_value = float('inf')
            for nei in [(1, j), (-1, j), (j, 1), (j, -1)]:
                nei_value = grid[nei[0]][nei[1]]
                if nei_value < min_value:
                    min_value = nei_value
                    starts[i] = nei
            for ni in range(N):
                dp[i][ni] = min_value

    # Trace back to find the minimum path
    ans = []
    curr = k
    while curr > 0:
        x, y = starts[curr]
        ans.append(grid[x][y])
        curr = (curr - 1) // 2

    return ans[::-1]  # Reverse the list to get the correct order
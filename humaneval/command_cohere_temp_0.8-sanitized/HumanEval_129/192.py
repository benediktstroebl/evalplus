def minPath(grid, k):
    N = len(grid)
    # initialize the dp matrix with -1
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    # queue for storing the path
    q = []
    # current path length
    cnt = 0
    # start from the bottom-left corner
    start = N - 1
    # iterate through k steps
    for _ in range(k):
        # find the minimum cell in the current row
        min_row = start
        for j in range(N):
            if dp[min_row][j] != -1 and dp[min_row][j] < dp[min_row][min_row]:
                min_row = j
        # update the path
        q.append(min_row)
        # update the current path length
        cnt += 1
        # update the dp matrix
        for i in range(N):
            if i == min_row:
                dp[i][min_row] = cnt
            elif grid[i][min_row] < grid[i][j]:
                dp[i][j] = dp[i][min_row] + 1
            else:
                dp[i][j] = dp[i][j] + 1
        # move to the next row
        start -= 1
    # return the sorted path
    return [grid[i][q[i]] for i in range(N)]
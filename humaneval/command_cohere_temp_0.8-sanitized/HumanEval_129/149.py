def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [i for i in range(N)]
    path = [[] for _ in range(k + 1)]  # List to store the path

    # Initialize the first column of the dp matrix and the start path
    for i in range(1, k + 1):
        dp[i][0] = 0
        path[i] = [start[0]]

    # Fill the dp matrix using a bottom-up approach
    for i in range(1, N):
        for j in range(1, k + 1):
            minVal = float('inf')
            for di in range(4):
                ni = i + di
                if ni < 0 or ni >= N:
                    continue
                for dj in range(4):
                    nj = j + dj
                    if nj < 1 or nj > k:
                        continue
                    neighbor = grid[ni][nj]
                    if neighbor < minVal:
                        minVal = neighbor
                        myPath = path[nj]
                        myStart = start[ni]
                        if di == 0 and dj == 0:
                            myStart = ni
                        path[nj] = myPath + [myStart]
                        start[ni] = myStart
                    elif neighbor == minVal:
                        myPath = path[nj]
                        myStart = start[ni]
                        if di == 0 and dj == 0:
                            myStart = ni
                        path[nj] = myPath + [myStart]
                        start[ni] = myStart

            dp[j][i] = minVal

    return path[k]
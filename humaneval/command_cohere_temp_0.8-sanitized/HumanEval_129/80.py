def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Create a 2D DP array to store the minimum paths for each cell
    dp = [[[float('inf')] * (N * N + 1) for _ in range(k + 1)] for _ in range(N + 1)]

    # Initialize the base case
    for i in range(N + 1):
        dp[i][0][1] = i

    # Fill in the DP array using a bottom-up approach
    for length in range(1, k + 1):
        for i in range(N + 1):
            for j in range(N * N, 0, -1):
                if dp[i][length - 1][j] == float('inf'):
                    continue
                minIndex = i
                minValue = j
                for x in range(i):
                    if dp[x][length - 1][j] != float('inf') and dp[x][length - 1][j] < dp[i][length - 1][j]:
                        minIndex = x
                        minValue = dp[x][length - 1][j]

                dp[i][length][minValue] = minIndex

    # Find the minimum path and return its values
    minPathIndices = []
    i, j = N, N * N
    while i > 0 and j > 0:
        if dp[i][k][j] != float('inf'):
            minPathIndices.append(dp[i][k][j])
            i, j = dp[i][k][j], 1
        else:
            j -= 1

    minPathIndices.reverse()
    return [grid[i][j] for i, j in minPathIndices]
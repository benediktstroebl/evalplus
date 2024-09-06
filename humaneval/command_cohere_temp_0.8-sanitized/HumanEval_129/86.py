def minPath(grid, k):
    n = len(grid)
    if k > n * n or k <= 0:
        return []

    # Create a 2D DP array to store the minimum paths ending in each cell.
    # The value -1 indicates that the cell is not reachable within k steps.
    dp = [[-1] * n for _ in range(n)]

    # Initialize the DP array with the starting cell values.
    for i in range(n):
        dp[i][grid[i][0] - 1] = 0

    # Fill in the DP array using a bottom-up approach.
    for len_path in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if dp[i][j] != -1 and (dp[i][j], grid[i][j]) < dp[i][j]:
                    # If we find a smaller path, update the cell value.
                    dp[i][j] = len_path, grid[i][j]

    # Trace back the minimum path from the goal cell.
    path = []
    i, j = n - 1, n * n - 1
    while i >= 0 and j >= 0:
        path.append(j + 1)
        if dp[i][j] == -1:
            j -= 1
        else:
            i, j = i - dp[i][j][0], j - dp[i][j][1]

    # Reverse the path to get the correct order.
    path.reverse()
    return path
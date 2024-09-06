def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1) for _ in range(k + 1)]

    # Initialize the first column as the smallest value
    for i in range(N):
        dp[0][i] = grid[i][0]

    for length in range(1, k + 1):
        for i in range(N):
            for j in range(N):
                # Check if we can move to the cell
                if (i, j) != start[length - 1]:
                    # Update the minimum value for the current length
                    dp[length][j] = min(dp[length][j], dp[length - 1][i] + grid[i][j])
                    # Update the starting position for the current length
                    start[length][j] = (i, j)

    # Traverse the dp list to find the answer
    answer = []
    i, j = start[k]
    while len(answer) < k:
        answer.append(grid[i][j])
        if (i, j) != start[k]:
            i, j = start[k]
        else:
            j = (j + 1) % N
            if j == i:
                i = (i + 1) % N

    # Remove duplicates and sort the list
    answer = list(set(answer))
    answer.sort()
    return answer
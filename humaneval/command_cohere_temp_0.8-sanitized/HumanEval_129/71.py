def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Create a 2D list to store the shortest path and initialize all paths as INF
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    dp[0][0] = 0

    # Use a queue for asynchronous path exploration
    queue = [(0, 0, [grid[0][0]])]  # (row, col, path)

    while queue:
        row, col, path = queue.pop(0)

        # Explore all 8 neighbors
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < N and 0 <= newCol < N:
                newPath = path + [grid[newRow][newCol]]
                if dp[newRow][newCol] > len(newPath) - k:
                    dp[newRow][newCol] = len(newPath) - k
                    queue.append((newRow, newCol, newPath))

    return dp[0][0]
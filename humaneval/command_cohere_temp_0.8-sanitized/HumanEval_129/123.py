def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and min path indices
    visited = [False] * (N * N)
    minPathIndices = [-1] * (N * N)

    def dfs(row, col, currentPathLength):
        if visited[row * N + col]:
            return

        visited[row * N + col] = True

        if currentPathLength == k:
            minPathIndices[row * N + col] = len(path)
            return

        for nei in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= nei[0] < N and 0 <= nei[1] < N and grid[nei[0]][nei[1]] != 0 and not visited[nei[0] * N + nei[1]]:
                path.append(grid[nei[0]][nei[1]])
                dfs(nei[0], nei[1], currentPathLength + 1)
                path.pop()

    path = []
    for i in range(N):
        for j in range(N):
            if not visited[i * N + j] and grid[i][j] != 0:
                dfs(i, j, 1)

    # Build the min path based on the tracked indices
    minPath = [grid[row][col] for row, col in zip(*minPathIndices)]
    return minPath
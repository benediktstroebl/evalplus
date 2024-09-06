def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and min path indices
    visited = [-1] * N
    minPath = [-1] * N
    minPathIndex = [-1] * N

    def dfs(row, col, currentPathLength):
        if currentPathLength >= k:
            return True  # Found a valid path of length k

        if visited[row] >= col:
            return False  # Already visited this cell

        visited[row] = col

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = row + dr, col + dc
            if 0 <= r < N and 0 <= c < N and grid[r][c] != 0 and not dfs(r, c, currentPathLength + 1):
                return False  # Reached a dead-end or found a better path

        # Found a valid path
        minPath[row] = col
        minPathIndex[row] = currentPathLength
        return True

    # Start the DFS from any cell (pick the top-left cell as the starting point)
    startRow, startCol = 0, 0
    if not dfs(startRow, startCol, 1):
        return []  # No valid path of length k found

    # Track the descending order of path lengths
    sortedPathIndices = sorted(enumerate(minPathIndex), key=lambda x: x[1])

    # Reconstruct the minimum path
    result = []
    row, col = sortedPathIndices[0][0], minPath[sortedPathIndices[0][0]]
    for i in range(k - 1, -1, -1):
        result.append(grid[row][col])
        row, col = sortedPathIndices[i][0], minPath[sortedPathIndices[i][0]]

    return result[::-1]  # Reverse the list to get the correct order
def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and previously seen cells for each row
    visited, previously = [[False] * (N * N) for _ in range(2)]
    
    # Initialize the path with the starting cell
    path = set()
    row, col = next((r, c) for r in range(N) for c in range(N) if not visited[r][c] and grid[r][c] <= k), None

    while k > 0 and col is not None:
        previously[row][col] = True  # Mark this cell as previously seen
        for nei in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
            if 0 <= nei[0] < N and 0 <= nei[1] < N and not previously[nei[0]][nei[1]] and grid[nei[0]][nei[1]] <= k:
                row, col = nei
                path.add(grid[row][col])
                k -= 1
                visited[row][col] = True
                previously[row][col] = False
        if not k and col is not None:
            col = None

    return list(path)
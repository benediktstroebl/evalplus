def minPath(grid, k):
    n = len(grid)
    visited = [False] * (n * n)
    queue = [(0, 0)]  # (row, col)
    path = []

    while queue:
        size = len(queue)
        for _ in range(size):
            row, col = queue.pop(0)
            if visited[row * n + col]:
                continue
            visited[row * n + col] = True

            # Append the current cell value to the path
            path.append(grid[row][col])

            # Explore neighboring cells in a counter-clockwise direction
            if col > 0 and not visited[row * n + col - 1]:
                queue.append((row, col - 1))
            if col < n - 1 and not visited[row * n + col + 1]:
                queue.append((row, col + 1))
            if row > 0 and not visited[row - 1 * n + col]:
                queue.append((row - 1, col))
            if row < n - 1 and not grid[row + 1][col] and not visited[row + 1 * n + col]:
                queue.append((row + 1, col))

    # Reverse the path if the desired length is odd
    if k % 2 == 1:
        path.reverse()

    return path[:k]
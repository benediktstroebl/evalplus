def minPath(grid, k):
    N = len(grid)
    visited = [set() for _ in range(N)]
    queue = [(0, 0)]  # (row, col)

    while queue:
        row, col = queue.pop(0)  # Dequeue

        # Base case: Found a path of length k
        if len(visited[row]) == k:
            path = []
            row, col = row, col
            while row >= 0 and row < N and col >= 0 and col < N:
                path.append(grid[row][col])
                if len(visited[row]) == k:
                    break
                row, col = (row + row_adj[0], col + row_adj[1])
            return path[::-1]  # Return reversed path

        visited[row].add(col)
        for nei in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Neigbors
            row_adj = nei[0], nei[1]
            new_col = col + row_adj
            if 0 <= new_col < N and new_col not in visited[row] and grid[row][new_col] != 0:
                queue.append((row, new_col))
                visited[row].add(new_col)

    return []  # No path of length k found
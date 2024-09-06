def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(-1, 0)]  # (-1, x) indicates the minimum path length and the x-th column

    while q:
        dist, col = q.pop()
        if dist > k:
            continue

        row = bisect.bisect_left(grid[col], dist + 1)
        if row == n:
            continue

        if (row, col) in visited:
            continue

        visited.add((row, col))
        q.append((dist + 1, col))
        q.append((dist + 1, col + 1))
        q.append((dist + 1, col - 1))

    return [grid[row][col] for row, col in visited]
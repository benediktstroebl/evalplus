def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(-1, 0)]  # (-1, cell) indicates the starting cell with value -1
    while len(q) > 0 and k > 0:
        x, y = q.pop()
        if x == -1:
            continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        k -= 1
        if x < n - 1:
            q.append((x + 1, y))
        if x > 0:
            q.append((x - 1, y))
        if y < n - 1:
            q.append((x, y + 1))
        if y > 0:
            q.append((x, y - 1))
    return [cell for cell in visited if cell != (-1, 0)]
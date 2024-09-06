def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(0, 0, grid[0][0])]
    while q:
        x, y, c = min(q, key=lambda xy_c: (xy_c[0] != x or xy_c[1] != y, xy_c[1], xy_c[2]))
        if len(visited) == k:
            return list(visited)
        visited.add(c)
        x += 1
        if 0 <= x < n and grid[x][y] not in visited:
            q.append((x, y, grid[x][y]))
        y += 1
        if 0 <= y < n and grid[x][y] not in visited:
            q.append((x, y, grid[x][y]))
    return []
def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(-1, 0)]  # (-1, x) indicates the minimum path of length x
    while q and k:
        x, y = min(q)[1:]
        if y == k:
            return [z for z in grid[x] if z not in visited and visited.add(z)]
        if x == -1:
            continue
        for dx, dz in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            z = grid[x][y + dx]
            if z not in visited and (y + dx + dz) <= k:
                q.append((x, y + dx + dz))
    return []
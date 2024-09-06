def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(0, 0, grid[0][0])]
    while q:
        x, y, val = q.pop()
        if len(visited) == k:
            return list(visited)
        visited.add(val)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nex = (x + dx, y + dy)
            if 0 <= nex[0] < n and 0 <= nex[1] < n and grid[nex[0]][nex[1]] not in visited:
                q.append((nex[0], nex[1], grid[nex[0]][nex[1]]))
    return []
def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    q = [(0, 0)]
    minPath = []

    while q:
        x, y = q.pop()
        if len(minPath) == k:
            return minPath

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newX, newY = x + dx, y + dy
            if 0 <= newX < n and 0 <= newY < n and (newX, newY) not in visited[x]:
                visited[x].add((newX, newY))
                q.append((newX, newY))
                if (newX, newY) in grid:
                    minPath.append(grid[newX][newY])
                    if len(minPath) == k:
                        return minPath
                else:
                    return []

    return []
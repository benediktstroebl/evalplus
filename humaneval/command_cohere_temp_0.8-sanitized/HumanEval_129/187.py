def minPath(grid, k):
    n = len(grid)
    dp = [None] * n
    q = deque([(0, 0, k) for _ in range(n)])
    visited = set()
    
    while q:
        x, y, dist = q.popleft()
        if dp[x] is not None and dist == dp[x][1]:
            continue
        if dist == k:
            path = []
            while x != 0 or y != 0:
                path.append(grid[x][y])
                if x > 0:
                    x -= 1
                else:
                    y -= 1
            path.reverse()
            return path
        if x > 0 and y > 0 and grid[x-1][y-1] not in visited:
            visited.add(grid[x-1][y-1])
            q.append((x-1, y-1, dist+1))
        if x < n-1 and y > 0 and grid[x+1][y-1] not in visited:
            visited.add(grid[x+1][y-1])
            q.append((x+1, y-1, dist+1))
        if x > 0 and y < n-1 and grid[x-1][y+1] not in visited:
            visited.add(grid[x-1][y+1])
            q.append((x-1, y+1, dist+1))
        if x < n-1 and y < n-1 and grid[x+1][y+1] not in visited:
            visited.add(grid[x+1][y+1])
            q.append((x+1, y+1, dist+1))
    
    return []
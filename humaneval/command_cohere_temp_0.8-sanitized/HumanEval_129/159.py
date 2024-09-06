def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dx, dy):
        if len(path) == k:
            return True, path

        # Explore all 4 directions
        for cc in (-1, 0, 1):
            for RR in (-1, 0, 1):
                newR, newC = r + RR, c + cc

                if 0 <= newR < N and 0 <= newC < N:
                    if (newR, newC) not in visited and grid[newR][newC] > 0 and dfs(newR, newC, path, visited, dx, dy):
                        dx, dy = (cc, RR)
                        return True, path + [grid[newR][newC]]
                    elif (newR, newC) not in visited:
                        visited.add((newR, newC))

    visited = set()
    startR, startC = 0, 0
    if dfs(startR, startC, [], visited, 0, 0):
        return list(reversed(sorted(path)))
    else:
        return []
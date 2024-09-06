def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, prev):
        if len(path) == k:
            return True, path

        if visited[r][c]:
            return False, path

        visited[r][c] = True

        # check all 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N and grid[newR][newC] > grid[r][c]:
                if dfs(newR, newC, path + [grid[newR][newC]], visited, (newR, newC)):
                    return True, path

        # if nothing better is found, add the current cell
        return False, path + [grid[r][c]]

    visited = [[False for _ in range(N)] for _ in range(N)]
    return dfs(0, 0, [], visited, (0, 0))[1]
def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, counter):
        if len(path) == k:
            return True, path

        if counter == k:
            return False, path

        visited[r][c] = True
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != path[-1] and not visited[nr][nc]:
                newPath = path + [grid[nr][nc]]
                if dfs(nr, nc, newPath, visited, counter + 1):
                    return True, newPath
        
        return False, path

    visited = [False] * N
    path = []
    if dfs(0, 0, [], visited, 0):
        return path
    else:
        return [1]
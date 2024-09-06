def minPath(grid, k):
    n = len(grid)
    def dfs(r, c, path, visited, cd):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return path
        visited[(r, c)] = 1
        cd[0] = grid[r][c]
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > cd[0]:
                newPath = dfs(nr, nc, path + [grid[nr][nc]], visited, cd[1:])
                if newPath:
                    return newPath
        return None
    
    cd = [grid[0][0]]
    visited = {(0, 0): 1}
    path = dfs(0, 0, [], visited, cd)
    return path
def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, prev_row, prev_col):
        if len(path) == k:
            return path
        if visited[r][c]:
            return path

        visited[r][c] = True
        path.append(grid[r][c])

        # Move in row direction
        if r != 0 and grid[r-1][c] not in path:
            dfs(r-1, c, path, visited, r, c)

        # Move in column direction
        if c != 0 and grid[r][c-1] not in path:
            dfs(r, c-1, path, visited, r, c)

        # Move diagonally
        if prev_row and prev_col:
            if grid[prev_row][c] < grid[r][prev_col]:
                dfs(prev_row, c, path, visited, prev_row, c)
            elif grid[prev_row][c] > grid[r][prev_col]:
                dfs(r, prev_col, path, visited, r, c)
            elif grid[prev_row][c] == grid[r][prev_col] and (r != N-1 or c != N-1):
                dfs(prev_row, c, path, visited, prev_row, c)
                dfs(r, prev_col, path, visited, r, c)

        return path

    start_row, start_col = 0, 0
    visited = [[False] * N for _ in range(N)]
    path = []
    k = min(k, len(grid[0]))
    return dfs(start_row, start_col, path, visited, start_row, start_col)
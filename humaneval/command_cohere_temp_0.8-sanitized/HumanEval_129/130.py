def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    def dfs(r, c, path, visited, prev_r, prev_c):
        if len(path) == k:
            return True, path

        if (r, c) in visited:
            return False, path

        visited[(r, c)] = True

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and dfs(nr, nc, path, visited, r, c):
                prev_r, prev_c = nr, nc
                path.append(grid[nr][nc])
                return True, path

        if prev_r is not None and prev_c is not None:
            path.append(grid[prev_r][prev_c])
            return True, path

        return False, path

    visited = {}
    min_path = []
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                if not dfs(i, j, min_path, visited, None, None):
                    return []
            if grid[i][j] == 1:
                return []

    return min_path
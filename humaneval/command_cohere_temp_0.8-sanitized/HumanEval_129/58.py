def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, cd):
        if len(path) == k:
            return path
        if visited[r][c]:
            return path
        visited[r][c] = True
        cd[0] = False
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc] and (
                (nr, nc) != (r, c-1) or cd[0]
            ):
                path.append(grid[nr][nc])
                cd[0] = True
                path = dfs(nr, nc, path, visited, cd)
                if len(path) == k:
                    return path
        return path

    visited = [[False] * N for _ in range(N)]
    cd = [False] * N
    return dfs(0, 0, [], visited, cd)
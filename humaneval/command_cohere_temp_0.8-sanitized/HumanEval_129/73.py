def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, cd):
        if len(path) == k:
            return True, path

        if (r, c) in visited:
            return False, path

        visited[r, c] = True

        # Try moving in all 4 directions
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > cd and not visited[nr][nc]:
                if dfs(nr, nc, path+[grid[nr][nc]], visited, grid[nr][nc]):
                    return True, path + [grid[nr][nc]]

        return False, path

    # Start the search from the highest value cell (should exist since each value appears once)
    start_r, start_c = next((r, c) for r, row in enumerate(grid) for c, cd in enumerate(row) if cd == max(grid[0]))
    visited = [[False] * N for _ in range(N)]
    return dfs(start_r, start_c, [], visited, max(grid[0]))[1]
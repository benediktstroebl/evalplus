def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return path
        visited[(r, c)] = True
        path_options = [path + [grid[r][c]]]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < N and 0 <= new_c < N and grid[new_r][new_c] > grid[r][c] and (new_r, new_c) not in visited:
                path_options.append(dfs(new_r, new_c, path + [grid[r][c]], visited, dp))
        min_path = min(path_options, key=lambda x: x[-1])
        dp[r][c] = min(dp[r][c] if (r, c) in dp else float('inf'), *min_path[1:])
        return min_path

    start_r, start_c = 0, 0
    visited = {(start_r, start_c)}
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    return dfs(start_r, start_c, [grid[start_r][start_c]], visited, dp)
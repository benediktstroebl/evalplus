def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return path
        visited[r, c] = True

        # Explore all possible moves from the current cell
        moves = []
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and (nr, nc) not in visited:
                moves.append((nr, nc))

        if not moves:
            return path

        # Sort moves by the value of the next grid cell and choose the smallest
        # This ensures that we choose the shortest path when multiple paths diverge
        moves.sort(key=lambda x: grid[x[0]][x[1]])

        for nr, nc in moves:
            newPath = dfs(nr, nc, path + [grid[nr][nc]], visited, dp)
            if newPath and len(newPath) == k:
                return newPath

        # If no valid path is found, choose any cell as the next step
        if len(moves) >= 1:
            dp[r][c] = min(moves, key=lambda x: x[0])
            return dfs(dp[r][c][0], dp[r][c][1], path, visited, dp)

        return None

    # Initialize the dp table and visited cells
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = []

    # Start the DFS from the first cell (0, 0)
    return dfs(0, 0, path, visited, dp)
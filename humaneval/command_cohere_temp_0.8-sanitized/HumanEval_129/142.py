def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True
        if (r, c) in visited:
            return False
        visited[r, c] = True

        # Explore all possible steps from current position
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and dfs(nr, nc, path+[grid[nr][nc]], visited, dp):
                return True
        
        # Store the minimum valid path ending at this point
        if not dp[r][c] or len(path) + 1 == dp[r][c][0]:
            dp[r][c] = [(len(path) + 1,) if len(path) + 1 == dp[r][c][0] else ()] + path
        for i, length in enumerate(dp[r][c]):
            if length == k:
                return True
            if length == (len(path) + 1):
                break
        return False

    # Initialize the dp table and visited positions
    dp = [[None for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                return [grid[i][j]] + minPath(grid, k-1)
    
    # Start the DFS from the cell with value 1
    return minPath(grid, k-1, 0, N-1) if k else []
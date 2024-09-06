def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True
        if (r, c) in visited:
            return False
        visited[r, c] = True

        # Try moving in all 4 directions
        if dfs(r-1, c, path+[grid[r-1][c]], visited, dp) or \
           dfs(r+1, c, path+[grid[r+1][c]], visited, dp) or \
           dfs(r, c-1, path+[grid[r][c-1]], visited, dp) or \
           dfs(r, c+1, path+[grid[r][c+1]], visited, dp):
            return True

        # If none of the 4 directions leads to a valid path,
        # then this cell cannot be part of the answer
        return False

    # Initialize visited and DP arrays
    visited = [[False for _ in range(N)] for _ in range(N)]
    dp = [[[False for _ in range(N)] for _ in range(N)] for _ in range(k+1)]

    # Initialize the path with the starting cell
    path = [grid[0][0]]

    # Find the valid path
    for i in range(1, k+1):
        for r in range(N):
            for c in range(N):
                if not visited[r, c] and not dp[i][r][c] and dfs(r, c, path, visited, dp):
                    path.append(grid[r][c])
                    dp[i+1][r][c] = True
    path.reverse()
    return path
def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True
        if (r, c) in visited:
            return False
        visited[(r, c)] = True

        # Check all 4 directions
        if dfs(r-1, c, path + [grid[r-1][c]], visited, dp) or \
           dfs(r+1, c, path + [grid[r+1][c]], visited, dp) or \
           dfs(r, c-1, path + [grid[r][c-1]], visited, dp) or \
           dfs(r, c+1, path + [grid[r][c+1]], visited, dp):
            return True

        # Store the furthest reachable position for each cell
        if len(path) > dp[r][c]:
            dp[r][c] = len(path)

        return False

    if k > N*N or k < 1:
        return []

    # Initialising the 2D dp values
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    path = []

    # Finding the k-length path
    visited = {}
    for r in range(N):
        for c in range(N):
            if not dfs(r, c, [], visited, dp):
                return []

    # Returning the lexicographically minimum path
    return sorted(path)
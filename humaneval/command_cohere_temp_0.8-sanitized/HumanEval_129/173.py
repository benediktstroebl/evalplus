def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True  # Found a valid path of length k
        if visited[r][c]:
            return False  # Already visited this cell

        # Explore each of the 4 possible directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N and grid[newR][newC] > grid[r][c] and not visited[newR][newC]:
                visited[newR][newC] = True
                if dfs(newR, newC, path + [grid[newR][newC]], visited, dp):
                    return True 
                visited[newR][newC] = False

        # If no valid path is found, mark this cell as blocked
        dp[r][c] = -1
        return False

    # Initialize a 2D boolean array to track visited cells
    visited = [[False for _ in range(N)] for _ in range(N)]
    # Initialize a 2D integer array to store the blocked cells
    dp = [[0 for _ in range(N)] for _ in range(N)]

    startR, startC = 0, 0
    if not dfs(startR, startC, [], visited, dp):
        return []  # No valid path found

    # Start from the unblocked cell with the smallest value and reconstruct the path
    minVal = min(grid[startR][startC:])
    path = [minVal] * (k - 1) + [minVal + 1]
    return path
def minPath(grid, k):
    n = len(grid)
    dp = [float('inf')] * n * n
    dist = [float('inf')] * n * n
    
    def dfs(i, j, step):
        if step == k:
            return grid[i][j]
        if dp[i * n + j] != float('inf') and dist[i * n + j] <= step:
            return dp[i * n + j]
        
        grid_ind = (i * n + j)

        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < n and 0 <= y < n and grid[x][y] != grid[i][j] and (x, y) != (i, j):
                    new_dist = dfs(x, y, step + 1)
                    if new_dist != float('inf') and new_dist < dist[grid_ind]:
                        dist[grid_ind] = new_dist
                        dp[grid_ind] = new_dist
                        return new_dist
        
        return float('inf')
    
    # Starting the search from the top-left cell.
    return dfs(0, 0, 1)
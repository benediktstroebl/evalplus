def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return None
        visited[(r, c)] = True

        # Explore all possible paths from this cell
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0 and (nr, nc) not in visited:
                neigPath = dfs(nr, nc, path + [grid[nr][nc]], visited, dp)
                if neigPath is not None:
                    if neigPath not in dp:
                        dp[neigPath] = 1
                    else:
                        dp[neigPath] += 1
                    if len(neigPath) == k:
                        return neigPath
        
        return None

    # Initialize dictionary to store the number of occurrences of each path
    dp = {}
    # Initialize visited dictionary
    visited = {}
    
    # Start from any cell (we choose the top-left cell arbitrarily)
    start = (0, 0)
    startPath = [grid[start[0]][start[1]]]
    return minPathHelper(startPath, k, dp, visited)
def minPathHelper(path, k, dp, visited):
    # Base case: If the path length is less than k, return it
    if len(path) < k:
        return path
    # If we have explored this path before, return the stored path
    if path in dp:
        return dp[path]
    # Initialize visited dictionary for this path
    visited[path] = 1
    
    # Explore all possible extensions of this path
    for nextCell in path:
        extendedPath = path + [nextCell]
        if len(extendedPath) == k:
            return extendedPath
        
        if extendedPath not in dp and nextCell > 0:
            # If we haven't explored this extension before, recursively explore it
            newPath = minPathHelper(extendedPath, k, dp, visited)
            if newPath:
                return newPath
    
    return None
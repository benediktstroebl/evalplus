def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and last seen cells
    visited = set()
    last_seen = {}

    def dfs(r, c, remaining):
        if remaining == 0:
            return grid[r][c]
        
        if (r, c) in visited:
            return last_seen[(r, c)]
        
        visited.add((r, c))
        last_seen[(r, c)] = dfs(r, c + 1, remaining)
        last_seen[(r, c)] = min(last_seen[(r, c)], dfs(r + 1, c, remaining))
        last_seen[(r, c)] = min(last_seen[(r, c)], dfs(r - 1, c, remaining))
        last_seen[(r, c)] = min(last_seen[(r, c)], dfs(r, c - 1, remaining))
        return last_seen[(r, c)]
    
    start_cell = (0, 0)
    return dfs(start_cell[0], start_cell[1], k)
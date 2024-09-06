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
            return 0
        
        visited.add((r, c))
        last_seen[(r, c)] = remaining
        
        # Explore all neighbors
        neighbors = [
            (r-1, c), (r+1, c), (r, c-1), (r, c+1)
        ]
        
        results = [0] * len(neighbors)
        for nr, nc in neighbors:
            results[neighbors.index((nr, nc))] = dfs(nr, nc, remaining-1)
        
        # Find the minimum result and the last seen state
        min_result = min(results)
        last_seen[(r, c)] = min(last_seen[(r, c)], results.index(min_result))
        
        return min_result
    
    # Start the DFS from the first cell
    start_cell = (0, 0)
    result = dfs(start_cell[0], start_cell[1], k-1)
    
    # Reconstruct the path
    path = [result]
    current = (start_cell[0], start_cell[1])
    while current in last_seen:
        next_pos = sorted((current, last_seen[current]))[0]
        path.append(dfs(next_pos[0], next_pos[1], k-1))
        current = next_pos
    path.reverse()
    return path
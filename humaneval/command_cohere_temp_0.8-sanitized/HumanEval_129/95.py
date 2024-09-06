def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and accumulated path indices
    visited = set()
    path = []
    
    # Start from the first row and column
    r, c = 0, 0

    while len(path) < k:
        # Check all 4 neighbors of the current cell
        for nr, nc in [(r, c), (r, c+1), (r, c-1), (r+1, c)]:
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                visited.add((nr, nc))
                path.append(grid[nr][nc])
                if len(path) == k:
                    break
        
        # If no valid path of length k can be found, return an empty list
        if len(path) == k:
            continue
        
        # Sort the path and remove duplicates (for lexicographic comparison)
        path = sorted(set(path))
        
        # Check if the first k cells form a valid path of length k
        if len(path) == k:
            return path

    return []
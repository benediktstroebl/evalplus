def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and finalized cells
    visited, finalized = set(), set()
    
    # Initialize starting cell and its value
    q = [(0, 0, grid[0][0])]
    
    while q:
        curr_row, curr_col, value = q.pop()  # Dequeue
        visited.add((curr_row, curr_col))
        
        if len(visited) == k:
            return [value] * k
        
        # Explore neighboring cells in prioritized order (anticlockwise)
        for nei_row, nei_col in [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)]:
            if 0 <= nei_row < N and 0 <= nei_col < N and grid[nei_row][nei_col] != value and (nei_row, nei_col) not in finalized:
                q.append((nei_row, nei_col, grid[nei_row][nei_col]))
                finalized.add((nei_row, nei_col))
    
    return []
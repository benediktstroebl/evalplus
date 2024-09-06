def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(-1, 0)]  # (-1, row) : first row is '0', last is 'n-1'
    
    while len(q) > 0:
        row, col = q.pop()
        if col == k-1:
            path = [grid[row][col]]
            break
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for nei in [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] != 0 and (nei[0], nei[1]) not in visited:
                q.append(nei)
    
    if path:
        return path
    else:
        return [0]
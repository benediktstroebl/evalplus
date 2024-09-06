def minPath(grid, k):
    n = len(grid)
    def dfs(r, c, path, visited, prev_r, prev_c):
        if len(path) == k:
            return path
        if (r, c) in visited:
            return path
        visited[(r, c)] = True
        path.append(grid[r-1][c-1])
        for nei in [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] > 0 and (nei[0], nei[1]) != (prev_r, prev_c) and dfs(nei[0], nei[1], path, visited, r, c):
                return path
        path.pop()
        return None
    
    path = []
    visited = {}
    root_node = (-1, -1)
    result = dfs(root_node[0], root_node[1], path, visited, root_node[0], root_node[1])
    return result if result else [0]
def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    stack = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(r, c, remaining):
        if remaining == 0:
            return True
        if (r, c) in stack:
            return False
        stack.append((r, c))
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] not in visited[r]:
                visited[nr].add(grid[nr][nc])
                if dfs(nr, nc, remaining-1):
                    return True
            elif dr == 0 and nc > 0 and grid[r][nc] == grid[r][nc-1]:
                visited[r].add(grid[r][nc])
                if dfs(r, nc-1, remaining-1):
                    return True
        stack.pop()
        return False
    
    start = 0
    # Start from the smallest cell to ensure the answer is unique
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start = max(start, i + j)
    return [grid[i][j] for i, j in zip(range(start), range(start))]
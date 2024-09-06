def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and finished cells in the minimum path
    visited, finished = set(), set()

    def dfs(r, c, remaining):
        if remaining == 0:
            finished.add((r, c))
            return True

        if (r, c) in visited:
            return False

        visited.add((r, c))
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and dfs(nr, nc, remaining-1):
                return True
        return False

    # Start the DFS from the first cell in the first row
    start_row, start_col = 0, 0
    if not dfs(start_row, start_col, k):
        return []

    # Track the values in the minimum path and return
    path = []
    while len(finished) > 0:
        fr, fc = finished.pop()
        path.append(grid[fr][fc])

    return list(reversed(path))
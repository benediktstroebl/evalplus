def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and previous cells for DFS
    dfs = [[False] * N for _ in range(N)]
    prev = [-1] * N

    def dfs_path(r, c, k, path):
        if k == 0:
            return path

        if dfs[r][c]:
            return None  # Path loop detected, skip

        dfs[r][c] = True

        # Explore all possible neighbor cells
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not dfs[nr][nc]:
                nei = dfs_path(nr, nc, k - 1, [grid[nr][nc]] + path)
                if nei:
                    prev[nr * N + nc] = (r, c)  # Save previous cell for later
                    return nei

        return None  # No valid path found, backtrack

    # Start DFS from any valid cell (not necessarily the first cell)
    start_cell = 0
    while not dfs[start_cell]:
        start_cell = (start_cell + 1) % N

    result = dfs_path(start_cell, 0, k, [])
    if not result:
        return []  # No valid path found

    # Reconstruct the path based on the 'prev' tracking
    path = []
    while result:
        r, c = prev[result.index(grid[r][c])]
        path.append(grid[r][c])
        result = result[:result.index(grid[r][c])]

    return path[::-1]  # Reverse the path to the original order
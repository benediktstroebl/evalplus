def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and minimized path indices
    visited = set()
    minimized = []
    dir_graph = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]  # Up, Right, Down, Left

    start_idx = 0
    row, col = grid[0][0], grid[0][0]

    for _ in range(k):
        if row > N - 1 or col > N - 1 or row < 0 or col < 0:
            break

        # Determine the most minimized valid adjacent cell
        min_dist = float('inf')
        min_idx = None
        for dr, dc in dir_graph:
            r = row + dr
            c = col + dc
            if 0 <= r < N and 0 <= c < N:
                dist = 1 + (r in visited or dc == 0) + (c in visited or dr == 0)
                if dist < min_dist:
                    min_dist = dist
                    min_idx = (r, c)

        if min_idx is None:
            break

        visited.add(min_idx)
        row, col = min_idx
        minimized.append(grid[row][col])

    return minimized[::-1] if minimized else []
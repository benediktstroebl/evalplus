def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and previous cells for DFS
    dfs = [[False] * N for _ in range(N)]
    dfs[0][0] = True

    # Initialize the answer path
    path = []
    stack = [0]

    while stack:
        curr = stack.pop()
        if dfs[curr][0] and not dfs[curr][1]:  # Unvisited and no previous
            for nxt in range(N):
                if grid[curr][nxt] != grid[dfs[curr][1]][nxt]:
                    dfs[nxt][0] = True
                    dfs[nxt][1] = curr
                    stack.append(nxt)
            if len(stack) == k:
                path = [grid[c][n] for c, n in zip(stack, range(k))]
                return path

    return []
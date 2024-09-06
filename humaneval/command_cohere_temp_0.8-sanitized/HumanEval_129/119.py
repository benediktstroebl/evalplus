def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    def dfs(r, c, path, visited, dp):
        if len(path) == k:
            return True  # Found a valid path of length k

        # Explore all possible moves from the current cell (r, c)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > grid[r][c] and (
                nr,
                nc,
            ) not in visited and dfs(nr, nc, path + [grid[nr][nc]], visited + [(nr, nc)], dp):
                return True

        # If no valid path is found, mark this cell as explored and revisit later
        if (r, c) not in visited:
            visited.add((r, c))
            dp[r][c] = k
        return False

    # Initialize a 2D DP array to store the optimal path length and track visited cells
    dp = [[float("inf")] * N for _ in range(N)]
    start = set()  # Track starting cells (all cells initially)
    visited = set()  # Track visited cells
    minLength = float("inf")

    # Find the shortest path
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1 and (r, c) not in visited:
                start.add((r, c))
                if dfs(r, c, [], visited, dp):
                    minLength = min(minLength, dp[r][c])

    # Build the answer list
    answer = []
    for r in range(N):
        for c in range(N):
            if dp[r][c] == minLength and grid[r][c] > 1:
                answer.append(grid[r][c])

    return answer if len(answer) == k else []
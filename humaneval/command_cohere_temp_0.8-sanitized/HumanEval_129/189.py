def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and minimized path cells
    visited = set()
    min_path = []

    def dfs(r, c, remaining):
        if remaining == 0:
            return True  # Reached the goal

        if (r, c) in visited:
            return False  # Already visited

        visited.add((r, c))

        # Explore each of the 4 possible directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0 and dfs(nr, nc, remaining - 1):
                min_path.append(grid[nr][nc])
                return True

        return False  # No valid path in this direction

    if not dfs(0, 0, k):
        return []

    # Sort the minimized path in ascending order
    min_path.sort()
    return min_path
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
k = 3
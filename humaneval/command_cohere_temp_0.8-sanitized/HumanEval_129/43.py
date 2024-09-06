def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and accumulated path indices
    visited = set()
    path = []

    def dfs(r, c, remaining):
        if remaining == 0:
            return True  # Reached the goal

        if (r, c) in visited:
            return False  # Already visited

        visited.add((r, c))

        # Check all 4 directions (up, down, left, right)
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not dfs(nr, nc, remaining - 1):
                path.append(grid[r][c])
                return True

        return False  # No valid path from this cell

    if not dfs(0, 0, k):
        return []

    return path[::-1]  # Return reversed path to maintain lexicographical order
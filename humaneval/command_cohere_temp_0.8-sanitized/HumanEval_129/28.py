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

        # Check all four directions (up, down, left, right)
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N and grid[newR][newC] != 0 and not dfs(newR, newC, remaining - 1):
                path.append(grid[r][c])
                return True

        return False  # No valid path from this cell

    if not dfs(0, 0, k):
        return []

    # Sort and return the lexicographically smallest k-length path
    return sorted(path)
k = 3
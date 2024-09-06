def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and previously seen values
    seen = set()
    path = []

    def dfs(r, c, remaining):
        if remaining == 0:
            return True  # Reached the goal

        if (r, c) in seen:
            return False  # Already visited

        seen.add((r, c))
        if grid[r][c] not in seen:
            path.append(grid[r][c])
            if dfs(r, c + 1, remaining):
                return True
            if dfs(r + 1, c, remaining):
                return True
            if dfs(r, c - 1, remaining):
                return True
            if dfs(r - 1, c, remaining):
                return True
        return False  # No valid path from this node

    if dfs(0, 0, k):
        return path[-k:]
    return []
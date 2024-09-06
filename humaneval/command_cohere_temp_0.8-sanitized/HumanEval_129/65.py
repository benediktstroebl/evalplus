def minPath(grid, k):
    n = len(grid)
    if k > n * n or k <= 0:
        return []

    # Track visited and finalized cells
    visited, finalized = set(), set()

    def dfs(r, c, remaining):
        if remaining == 0:
            return True  # Reached the goal

        if (r, c) in finalized:
            return False  # Already visited

        if (r, c) in visited:
            return False  # Circular dependency

        visited.add((r, c))

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0 and (nr, nc) not in finalized:
                if dfs(nr, nc, remaining-1):  # Recursion
                    return True

                visited.remove((r, c))  # Backtrack
                finalized.add((nr, nc))
                visited.add((nr, nc))
                finalized.add((r, c))
                return True

        return False  # No valid path

    # Start the DFS from the first cell (r=0, c=0)
    if dfs(0, 0, k):
        return [grid[r][c] for r, c in sorted(finalized, key=lambda x: x[0] * n + x[1])]
    else:
        return []
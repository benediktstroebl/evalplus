def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and finished cells in the minimum path
    visited, finished = set(), set()

    def dfs(r, c, remaining):
        if remaining == 0:
            finished.add((r, c))
            return

        # Explore all possible moves from the current cell
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and (nr, nc) != (r, c):
                visited.add((nr, nc))
                dfs(nr, nc, remaining-1)

    # Start the DFS from the first cell in the grid
    dfs(0, 0, k)

    # Convert the coordinate pairs to integers and sort them
    finish_order = sorted(finished, key=lambda x: (x[0], -x[1]))
    return [grid[r][c] for r, c in finish_order]
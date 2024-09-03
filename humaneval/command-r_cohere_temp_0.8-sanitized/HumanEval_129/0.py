def minPath(grid, k):
    """
    Finds the minimum path of length k in the grid.

    Parameters:
        - grid (list of lists): A grid with N rows and N columns.
        - k (int): The length of the path.

    Returns:
        - list: An ordered list of the values on the cells 
            that the minimum path goes through.
    """
    N = len(grid)
    path = []
    visited = set()

    def dfs(x, y, current_path):
        if len(current_path) == k:
            path.extend(current_path)
            return

        current_path.append(grid[x][y])
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, current_path[:])
                visited.remove((nx, ny))
        current_path.pop()

    for x in range(N):
        for y in range(N):
            if (x, y) not in visited:
                visited.add((x, y))
                dfs(x, y, [grid[x][y]])
                visited.remove((x, y))

    return path
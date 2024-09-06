
def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    N = len(grid)

    def dfs(grid, i, j, k, grid_repr, visited, min_path, path):
        if i < 0 or j < 0 or i >= N or j >= N or grid[i][j] == -1 or visited[i][j]:
            return
        if k == 0:
            path.append(grid[i][j])
            min_path.append(path.copy())
            path.pop()
            return

        grid_repr[i][j] = -1
        visited[i][j] = True
        path.append(grid[i][j])
        dfs(grid, i + 1, j, k - 1, grid_repr, visited, min_path, path)
        dfs(grid, i - 1, j, k - 1, grid_repr, visited, min_path, path)
        dfs(grid, i, j + 1, k - 1, grid_repr, visited, min_path, path)
        dfs(grid, i, j - 1, k - 1, grid_repr, visited, min_path, path)
        grid_repr[i][j] = grid[i][j]
        visited[i][j] = False
        path.pop()

    visited = [[False] * N for _ in range(N)]
    min_path = []
    path = []
    grid_repr = [[None] * N for _ in range(N)]
    min_value = sys.maxsize
    for i in range(N):
        for j in range(N):
            dfs(grid, i, j, k, grid_repr, visited, min_path, path)
    for path in min_path:
        min_value = min(min_value, reduce(lambda a, b: a * 10 + b, path))
    return [int(x) for x in str(min_value)]



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
    def getMinPathHelper(grid, visited, path, k, row, col, total_grid_rows, total_grid_cols):
        if k == 0:
            return

        # avoid revisiting the cell
        if visited[row][col]:
            return

        # mark current cell as visited
        visited[row][col] = True

        # add current cell's value to the path
        path.append(grid[row][col])

        # check for the minimum path
        if k == 1:
            return

        # consider all possible neighbors
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # ignore the cell if it goes out of the grid
                if i < 0 or i >= total_grid_rows or j < 0 or j >= total_grid_cols:
                    continue
                # ignore the cell if it is not a neighbor of the current cell
                if not (i == row and j == col - 1 or i == row and j == col + 1 or
                        i == row + 1 and j == col or i == row - 1 and j == col):
                    continue
                getMinPathHelper(grid, visited, path, k - 1, i, j, total_grid_rows, total_grid_cols)

    # get number of rows and cols from the grid
    total_grid_rows = len(grid)
    total_grid_cols = len(grid[0])

    # call the helper function with initial values
    visited = [[False for _ in range(total_grid_cols)] for _ in range(total_grid_rows)]
    path = []
    getMinPathHelper(grid, visited, path, k, 0, 0, total_grid_rows, total_grid_cols)
    return path


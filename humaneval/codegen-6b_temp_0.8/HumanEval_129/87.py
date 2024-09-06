
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
    grid_len = len(grid)
    if k == 0:
        return []
    elif k == 1:
        return [min(grid[0])]

    total_n = sum(grid_len * grid_len for _ in range(grid_len))
    if k > total_n:
        return []

    min_grid = [float('inf')] * grid_len
    min_path = [None] * k

    curr_path = (0, 0)
    curr_grid = grid[curr_path[1]][curr_path[0]]
    min_grid[curr_path[0]] = curr_grid
    min_path[0] = grid[curr_path[1]][curr_path[0]]

    for row in range(1, grid_len):
        for col in range(grid_len):
            next_path = (col, row)
            next_grid = grid[next_path[1]][next_path[0]]
            if next_grid < curr_grid:
                curr_path = next_path
                curr_grid = next_grid
            elif col > 0 and next_grid < min_grid[col - 1]:
                min_grid[col] = next_grid
                min_path[col] = next_path
            elif col > 0:
                if min_grid[col - 1] < next_grid < min_grid[col]:
                    min_grid[col] = next_grid
                    min_path[col] = next_path

            if row > 0 and next_grid < min_grid[row - 1]:
                min_grid[row] = next_grid
                min_path[row] = next_path

    return [grid[row][col] for row, col in min_path]


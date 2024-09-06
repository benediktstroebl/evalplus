
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
    def is_legal_cell(grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    if k <= 0:
        raise ValueError("k must be >= 1")

    N = len(grid)
    M = len(grid[0])

    min_path = [None] * k
    # We are starting from the top left corner, so we have to make our first
    # step towards the top right corner.
    # NOTE: grid[0][0] == grid[0][1] == grid[1][0]
    cur_row = 0
    cur_col = 1

    for i in range(k):
        # Choose the direction of the next cell
        if grid[cur_row][cur_col] <= grid[cur_row][cur_col - 1]:
            cur_col -= 1
        else:
            cur_row += 1
        # After choosing the direction of the next cell, update min_path
        min_path[i] = grid[cur_row][cur_col]

    # If there are more steps left, we know we have to choose the direction that
    # minimizes the next cell value.
    # For example, if grid[cur_row][cur_col] == 3 and grid[cur_row + 1][cur_col]
    # == 2 and grid[cur_row][cur_col - 1] == 4, we have to choose the second path
    # because the next cell value is going to be grid[cur_row + 1][cur_col]
    # (i.e. 2), and not grid[cur_row][cur_col - 1] (i.e. 4).
    for i in range(k, N * M):
        if is_legal_cell(grid, cur_row - 1, cur_col):
            if grid[cur_row - 1][cur_col] <= grid[cur_row][cur_col - 1]:
                cur_row -= 1
        if is_legal_cell(grid, cur_row, cur_col + 

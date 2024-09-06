
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
    # base case
    if len(grid) == 1 and len(grid[0]) == 1:
        return [grid[0][0]]

    if len(grid) <= k or len(grid[0]) <= k:
        return None

    # get the min/max number of the rows
    min_rows = len(grid)
    max_rows = len(grid)
    for rows in grid:
        if len(rows) < min_rows:
            min_rows = len(rows)
        if len(rows) > max_rows:
            max_rows = len(rows)

    # get the min/max number of the cols
    min_cols = len(grid[0])
    max_cols = len(grid[0])
    for cols in zip(*grid):
        if len(cols) < min_cols:
            min_cols = len(cols)
        if len(cols) > max_cols:
            max_cols = len(cols)

    # print(min_rows, max_rows, min_cols, max_cols)
    # O(n^2 *k) and O(n*k)
    # dp = [[[0] * (max_cols+1) for _ in range(max_rows+1)] for _ in range(k+1)]
    # # print(dp)
    # for col in range(min_cols, max_cols+1):
    #     # print(col)
    #     for row in range(min_rows, max_rows+1):
    #         # print(row)
    #         for c in range(1, col+1):
    #             # print(c)
    #             dp[0][row][col] = 0
    #             if row == 1:
    #                 dp[0][row][col] = grid[row-1][col-1]
    #             else:
    #                 dp[0][row][col] = min(dp[0][row][col], dp[0][row-1][col-1])
    #
    # # print(dp)
    # for
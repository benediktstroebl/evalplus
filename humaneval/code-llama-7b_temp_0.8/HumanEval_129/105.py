
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
    # finds the minimum path of length k in a grid
    # k: the length of the path
    # grid: a two-dimensional array of integers representing the grid
    # returns: the minimum path represented as an array of integers
    # we have n rows and n columns
    rows = len(grid)
    cols = len(grid[0])
    # k >= rows + cols
    assert k >= rows + cols, 'k is too small'
    # k >= 2
    assert k >= 2, 'k is too small'
    # k <= n * n
    assert k <= rows * cols, 'k is too large'
    # initialize dp table
    # dp[i][j][k] = the minimum path length of a path of length k ending at i, j
    dp = [[[-1 for _ in range(rows + cols)] for _ in range(rows + cols)]
          for _ in range(rows + cols)]
    # fill the first column
    for i in range(rows + cols):
        dp[0][i][0] = 0
    # fill the first row
    for j in range(rows + cols):
        dp[j][0][0] = 0
    # fill the dp table
    # dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1])
    #                min path length of a path of length k ending at i, j
    for i in range(1, rows + cols):
        for j in range(1, rows + cols):
            if i < cols:
                dp[i][j][i] = dp[i - 1][j][i - 1]
            if j < rows:
                dp[i][j][j] = dp[i][j - 1][j - 1]
            if i < cols and j < rows:
                dp[i][j][i + j] = min(dp[i - 1][j][i - 1], dp[i][j - 1][j - 1])
    # retrieve the minimum path length
    i, j,

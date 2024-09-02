
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

    # The number of rows and columns in the grid.
    n = len(grid)
    # The length of the minimum path.
    m = n * n
    # The lexicographically minimal path.
    minPath = [0] * m
    # The lexicographically largest path.
    maxPath = [0] * m
    # A list to store the lexicographically largest path from the root cell.
    maxCellPath = [0] * k
    # A list to store the lexicographically smallest path from the root cell.
    minCellPath = [0] * k

    # Populate the initial values of the minPath and maxPath arrays.
    for i in range(n):
        minPath[i] = grid[i][0]
        maxPath[i] = grid[i][0]
    for i in range(n):
        minPath[i + n * (n - 1)] = grid[n - 1][i]
        maxPath[i + n * (n - 1)] = grid[n - 1][i]
    for i in range(1, n - 1):
        minPath[i * n] = grid[0][i]
        maxPath[i * n] = grid[0][i]
        minPath[(i + 1) * n - 1] = grid[i][n - 1]
        maxPath[(i + 1) * n - 1] = grid[i][n - 1]
    minPath[0] = grid[0][0]
    maxPath[0] = grid[0][0]
    minPath[n * n - 1] = grid[n - 1][n - 1]
    maxPath[n * n - 1] = grid[n - 1][n - 1]

    # Compute the lexicographically largest path.
    for i in range(1, n):
        for j in range(1, n):
            maxPath[i * n + j] = max(maxPath[(i - 1) * n + j], maxPath[i * n + j - 1]) + grid[i][j]

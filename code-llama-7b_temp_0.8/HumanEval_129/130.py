
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
    # calculate the number of rows and cols in grid
    n = len(grid)
    m = len(grid[0])

    # calculate the sum of all elements in grid
    sum = 0
    for i in grid:
        for j in i:
            sum += j

    # since we know that all elements in grid are distinct
    # we know that the smallest path must either go across
    # or down in the grid.
    # so we make a 2-D array dp where dp[i][j] stores the
    # minimum sum path going from the top left of the grid
    # to the point (i,j)
    dp = [[float("inf") for _ in range(m)] for _ in range(n)]

    # first dp[0][0] must be equal to the value of the
    # top left element in the grid
    dp[0][0] = grid[0][0]

    # now the problem reduces to finding the minimum sum path
    # going from the top left to the bottom right. We do this
    # by following the following steps :

    # 1. Fill all cells of the first row of dp except the
    #    first one with the values in the first row of grid
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 2. Fill all cells of the first column of dp except the
    #    first one with the values in the first column of grid
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 3. Fill all the remaining cells in dp with the minimum
    #    sum path going from (i,j) to (i-1,j-1)
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # 

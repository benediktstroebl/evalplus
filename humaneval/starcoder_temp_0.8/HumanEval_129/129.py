
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
    n = len(grid)

    # dp[i][j][k] := min path sum from grid[0][0] to grid[i][j] with k moves
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    # initialize the first row
    for j in range(n):
        dp[0][j][0] = grid[0][j]

    # initialize the first column
    for i in range(n):
        dp[i][0][0] = grid[i][0]

    for i in range(1, n):
        for j in range(1, n):
            for m in range(1, k + 1):
                if i > 0:
                    dp[i][j][m] = min(dp[i - 1][j][m], dp[i][j][m - 1]) + grid[i][j]
                else:
                    dp[i][j][m] = dp[i][j][m - 1] + grid[i][j]

    # get the min path sum for k moves
    min_val = min(dp[n - 1][j][k] for j in range(n))

    # get the index of the min path sum
    min_idx = None
    for j in range(n):
        if dp[n - 1][j][k] == min_val:
            min_idx = j

    # return the values on the min path
    return [grid[n - 1][min_idx]] + [grid[i][min_idx - 1] for i in range(n - 1, 0, -1)]

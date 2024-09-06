
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
    t = [[0] * n for _ in range(n)]
    t[0][0] = grid[0][0]
    # compute the min path to reach all the cells
    for i in range(1, n):
        t[i][0] = grid[i][0] + t[i - 1][0]
    for j in range(1, n):
        t[0][j] = grid[0][j] + t[0][j - 1]
    for i in range(1, n):
        for j in range(1, n):
            t[i][j] = grid[i][j] + min(t[i - 1][j], t[i][j - 1])
    # now find the minimum path
    v = [[0] * (k + 1) for _ in range(n)]
    v[0][0] = t[n - 1][n - 1]
    for i in range(1, n):
        v[i][0] = t[n - 1][i - 1] + v[i - 1][0]
    for j in range(1, n):
        v[0][j] = t[j - 1][n - 1] + v[0][j - 1]
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, min(i, j) + 1):
                v[i][j] = min(
                    v[i][j],
                    t[i - k][j - k] + v[i - k][j] + v[i][j - k] - v[i - k][j - k],
                )
    return path_backtrack(grid, k, v, n - 1, n - 1)


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
    # for each cell, what is the minimum number of steps to reach it from the
    # starting point?
    # what is the smallest number of steps such that we can reach each cell?
    # this is the shortest path from the starting point
    # to find the minimum path
    # can we use dynamic programming to solve it?
    # can we use memoization?
    # what is the time complexity of the current solution?
    # what is the time complexity of the optimal solution?
    # can we improve the time complexity?
    # what is the space complexity of the current solution?
    # what is the space complexity of the optimal solution?
    # can we improve the space complexity?

    n = len(grid)
    M = n * n

    def dist(i, j):
        return i * n + j

    DP = [[float("inf") for _ in range(k + 1)] for _ in range(n * n)]
    DP[0][0] = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, k + 1):
                d = dist(i, j)
                DP[d][k] = min(
                    DP[d][k], DP[dist(i - 1, j)][k - 1] + grid[i][j]
                )
                DP[d][k] = min(
                    DP[d][k], DP[dist(i, j - 1)][k - 1] + grid[i][j]
                )

    best = M
    for i in range(n):
        for j in range(n):
            for k in range(1, k + 1):
                best = min(best, DP[dist(i, j)][k])
    return [i % M + 1 for i in range(best)]


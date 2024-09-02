
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
    # Initialization
    N = len(grid)
    dp = [[float("inf")]*N for i in range(k+1)]
    # Base case:
    # 1. The number of cells in the grid is at most k
    # 2. The minimum path of length 1 must start from the first row or column
    for i in range(N):
        dp[1][i] = grid[0][i]
    # dp[1][0] = grid[0][0]

    # Fill the dp table:
    for i in range(2, k+1):
        for j in range(N):
            candidates = [dp[i-1][j]]
            # If it's not the first row or column
            if j != 0:
                candidates.append(dp[i-1][j-1])
            if j != N-1:
                candidates.append(dp[i-1][j+1])
            dp[i][j] = min(candidates)
    return dp[k]


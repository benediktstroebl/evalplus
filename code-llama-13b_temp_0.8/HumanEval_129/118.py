
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

    R = len(grid)
    C = len(grid[0])

    grid = [[grid[i][j] for j in range(C)] for i in range(R)]

    dp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            dp[r][c] = grid[r][c]
            if c != 0:
                dp[r][c] += dp[r][c-1]
            if r != 0:
                dp[r][c] += dp[r-1][c]
            if r and c:
                dp[r][c] -= dp[r-1][c-1]

    def helper(r, c, k):
        if (r == R-1 and c == C-1) or k < 0:
            return []

        if r == R-1:
            return helper(r, c+1, k)
        if c == C-1:
            return helper(r+1, c, k)

        dp_rc = dp[r][c]
        if c != 0:
            dp_rc -= dp[r][c-1]
        if r != 0:
            dp_rc -= dp[r-1][c]
        if r and c:
            dp_rc += dp[r-1][c-1]

        return [dp_rc] + helper(r, c+1, k-1) if dp_rc < dp[r][c+1] + dp[r+1][c] else [dp[r][c+1] + dp[r+1][c]] + helper(r+1, c, k-1)

    return helper(0, 0, k)


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
    if len(grid) == 0:
        return []
    N = len(grid)
    M = len(grid[0])

    # Initialize dp[i][j][k] to be equal to the minimum path
    # of length k from (0, 0) to (i, j)
    dp = [[[None for _ in range(k+1)] for _ in range(M)] for _ in range(N)]
    # Note that dp[i][j][0] is always 0.

    # Bottom-up calculation
    for i in range(N):
        for j in range(M):
            for k in range(1, k+1):
                if i == 0 and j == 0:
                    dp[i][j][k] = grid[i][j]
                elif i == 0:
                    dp[i][j][k] = dp[i][j-1][k-1] + grid[i][j]
                elif j == 0:
                    dp[i][j][k] = dp[i-1][j][k-1] + grid[i][j]
                else:
                    dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1]) + grid[i][j]

    # Start at the bottom-right corner
    # and follow the minimum-cost path up and left.
    path = []
    i, j, k = N-1, M-1, k
    while k >= 0:
        # If the only option is to move left, do it and continue
        if i == 0:
            path.append(dp[i][j][k])
            j -= 1
            k -= 1
        # If the only option is to move up, do it and continue
        elif j == 0:
            path.append(dp[i][j][k])
            i -= 1
            k -= 1
        # Otherwise, move up or left depending on which is cheaper
        else:
            if dp[i-1][j

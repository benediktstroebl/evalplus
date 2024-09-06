
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
    """
    # First, some simple cases
    if not grid or not grid[0]:
        return []
    if k <= 0:
        return []
    if k == 1:
        return [min(grid[0])]
    if k == 2:
        return [min(grid[0] + grid[1])]

    N = len(grid)

    # Initialize data structure
    # Store the minimum path from top-left to (i,j)
    # (i,j) will have the path with length k
    # Entry at (i,j) will be stored in dp[i][j][k]
    # Since we want to solve the problem in O(K) space, we will use dp in a smart way
    # dp[i][j][k] will store (1) the minimum path from (0,0) to (i,j) and the length
    # is k, or (2) the minimum path from (0,0) to (i,j) and the length is less than k
    dp = [[[] for j in range(N)] for i in range(N)]

    for i in range(N):
        dp[i][i] = [[grid[i][i]], 1]

    for k in range(2, k+1):
        for i in range(N):
            for j in range(N):
                if i == j:
                    dp[i][j] = [[grid[i][j]], 1]
                else:
                    dp[i][j] = [[], k]
                    for ni in range(i-1, i+2):
                        for nj in range(j-1, j+2):
                            if ni >= 0 and nj >= 0 and ni < N and nj < N:
                                if dp[ni][nj][1] + 1 < dp[i][j][1]:
                                    dp[i][j][0] = dp[ni][nj][0]
                                    dp[i][j][1] = dp[ni][nj][1] + 1
                                elif dp

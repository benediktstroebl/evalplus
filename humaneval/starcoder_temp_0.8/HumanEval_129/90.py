
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

    if not grid or len(grid) == 0 or not grid[0] or len(grid[0]) == 0:
        return []

    row = len(grid)
    col = len(grid[0])

    dp = [[0] * col for _ in range(row)]

    # initialize the minimum values
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[0][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][0]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # minPath is the minimum path in the grid
    minPath = []
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if i == row - 1 and j == col - 1:
            minPath.append(grid[i][j])
        elif i == row - 1:
            minPath.append(dp[i][j - 1] - grid[i][j])
        elif j == col - 1:
            minPath.append(dp[i - 1][j] - grid[i][j])
        else:
            if dp[i - 1][j] - grid[i][j] == dp[i][j - 1] - grid[i][j]:
                minPath.append(dp[i][j - 1] - grid[i][j])
            else:
                minPath.append(dp[i - 1][j] - grid[i][j])

        if k == len(minPath):
            break

        if dp[i - 1][j] < dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return minPath[::-1]

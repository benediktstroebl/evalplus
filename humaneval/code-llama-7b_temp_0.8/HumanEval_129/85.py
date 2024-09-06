
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
    rows = len(grid)
    cols = len(grid[0])
    dp = [[[float('inf')] * (k + 1) for j in range(cols)] for i in range(rows)]
    # populate the leftmost column in the dp table
    for row in range(rows):
        dp[row][0][1] = 0
    # populate the topmost row in the dp table
    for col in range(cols):
        dp[0][col][1] = 0
    # populate the rest of the dp table
    for row in range(1, rows):
        for col in range(1, cols):
            for step in range(1, k + 1):
                dp[row][col][step] = min(dp[row - 1][col][step - 1],
                                         dp[row][col - 1][step - 1])
                dp[row][col][step] += grid[row][col]
    # find the minimum sum at the end of the dp table
    res = float('inf')
    for step in range(1, k + 1):
        res = min(res, dp[rows - 1][cols - 1][step])
    # retrieve the minimum sum from the dp table
    path = [float('inf')] * k
    path[k - 1] = res
    row, col, step = rows - 1, cols - 1, k - 1
    while step > 1:
        if dp[row - 1][col][step - 1] <= dp[row][col - 1][step - 1]:
            path[step - 1] = grid[row - 1][col]
            row -= 1
        else:
            path[step - 1] = grid[row][col - 1]
            col -= 1
        step -= 1
    return path



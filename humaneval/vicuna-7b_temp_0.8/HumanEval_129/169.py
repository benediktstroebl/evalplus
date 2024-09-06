
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
    if not grid:
        return []
    grid = [int(i) for i in grid]
    dp = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    dp[0][0] = 1
    dp[0][i] = 0 for i in range(1, len(grid))
    dp[0][grid[0]] = 1
    for i in range(1, len(grid)):
        dp[i][0] = dp[i-1][0] + grid[i]
    for j in range(1, len(grid)):
        dp[0][j] = min(dp[0][j], dp[0][j-1] + grid[j])
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i] + 1)
    minpath = []
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            if dp[i][j] == k:
                minpath.append(grid[i])
    return minpath

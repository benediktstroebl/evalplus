
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
    grid = [list(row) for row in grid]
    dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = grid[0][0]
    dp[0][1] = grid[0][1]
    dp[0][2] = grid[0][2]
    for i in range(2, N+1):
        for j in range(1, i):
            for k in range(1, N+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                dp[i][j] = max(dp[i][j], dp[i][j-1] + dp[i-1][k] + dp[j][k-1] + dp[i-1][k-1])
    k_paths = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                path = [grid[i][j]]
                path_len = 1
                while path_len <= k:
                    path_len = dp[i][j]
                    path_len_less = dp[i][j] - path_len
                    path = path + list(path_less.keys())[path_len_less.index(min(path_less))]
                k_paths.append(path)
    return k_paths


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
    n, m = len(grid[0]), len(grid)
    if k >= n * m:
        return [grid[row][col] for row in range(m) for col in range(n)]

    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    dp_idx = {(0, 0): 0}

    def get_dp(row, col):
        if (row, col) not in dp_idx:
            dp_idx[(row, col)] = len(dp)
            dp.append([0] * n)
            for i in range(row, m):
                dp[dp_idx[(row, col)]][i] = dp[dp_idx[(row, col)] - 1][i] + grid[i][col]
            for j in range(col, n):
                dp[dp_idx[(row, col)]][j] = dp[dp_idx[(row, col)] - 1][j] + grid[row][j]
        return dp[dp_idx[(row, col)]]

    min_path = [get_dp(0, 0)]
    while len(min_path) < k:
        min_path.append(get_dp(0, 1))
    return min_path[-1][:-1]


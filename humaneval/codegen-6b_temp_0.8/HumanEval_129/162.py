
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
    if k == 0:
        return []
    N = len(grid)
    if N == 1:
        return grid[0]
    # dp[i][j] means the minimum path in grid[i][j]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    # min_path[i][j] means the minimum path in grid[i][j]
    min_path = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                min_path[i][j] = grid[i][j]
            elif i == 0:
                # dp[i][j] = dp[i][j-1] + grid[i][j]
                dp[i][j] = grid[i][j] + min_path[i][j-1]
                min_path[i][j] = min_path[i][j-1]
            elif j == 0:
                # dp[i][j] = dp[i-1][j] + grid[i][j]
                dp[i][j] = grid[i][j] + min_path[i-1][j]
                min_path[i][j] = min_path[i-1][j]
            else:
                dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])
                min_path[i][j] = min(min_path[i][j-1], min_path[i-1][j])

    return min_path[N-1][N-1]


assert minPath([[1,2,3], [4,5,6], [7,8,9]], 3) == [1, 2, 1]
assert minPath([[5,9,3], [4,1,6], [7,8,2]], 1) == [1]

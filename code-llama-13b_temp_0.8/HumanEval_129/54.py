
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
    def is_valid(x, y, N):
        if x < 0 or x >= N or y < 0 or y >= N:
            return False
        return True
    
    N = len(grid)

    # dp[i][j] means min path with len = i starting at (j, i)
    # dp[i][j] = min(dp[i-1][k] + grid[j][k], dp[i-1][k-1] + grid[j][k-1])
    # where 0 <= k <= j < N

    dp = [[0]*N for _ in range(k+1)]

    # init for k = 0
    for j in range(N):
        dp[0][j] = 1

    for i in range(1, k+1):
        for j in range(N):
            min_ = 10**6
            for k in range(j+1):
                if is_valid(j-1, k, N) and dp[i-1][k] < min_:
                    min_ = dp[i-1][k]
                if is_valid(j, k-1, N) and dp[i-1][k-1] < min_:
                    min_ = dp[i-1][k-1]
            dp[i][j] = min_ + grid[j][k]

    return dp[-1]

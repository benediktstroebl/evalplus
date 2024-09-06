
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
    # check that grid and k are valid
    N = len(grid)
    if N <= 1: return False
    if k < 1 or k > N*N: return False
    # check that k is a possible solution
    visited = [0]*N
    total = N*N
    for i in range(N):
        for j in range(N):
            visited[grid[i][j] - 1] += 1
    count = 0
    for i in range(N):
        if visited[i] > 0:
            count += visited[i]
    if count < k: return False
    # set up dp
    dp = [[0]*N for _ in range(N)]
    # fill in starting values
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                continue
            if i == 0:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
                continue
            if j == 0:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    # get the result
    result = []
    for _ in range(k):
        result.append(dp[N - 1][N - 1])
        if N == 2:
            return result
        if dp[N - 2][N - 1] == dp[N - 1][N - 2]:
            dp[N - 2][N - 1] = 0
            dp[N - 1][N - 2] = 0
            N -= 1
            continue
        if dp[N - 1][N - 2] < dp[N - 2][N - 1]:
            dp[N - 2][N - 1] = 

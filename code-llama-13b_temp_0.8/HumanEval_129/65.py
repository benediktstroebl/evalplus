
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
        return None
    
    N = len(grid)
    k = min(k, N*N)
    # memo = [[0] * N for _ in range(N)]
    memo = [0] * N
    # only need to store the last row
    # memo = [0] * N
    # dp[i][j] = length of min path for i, j
    dp = [[0] * N for _ in range(N)]

    def dfs(i, j, k):
        if not k:
            return 1
        
        if dp[i][j]:
            return dp[i][j]
        res = 0
        if i > 0:
            res = max(res, dfs(i-1, j, k-1))
        if i < N-1:
            res = max(res, dfs(i+1, j, k-1))
        if j > 0:
            res = max(res, dfs(i, j-1, k-1))
        if j < N-1:
            res = max(res, dfs(i, j+1, k-1))
        dp[i][j] = res + 1
        return res + 1
    
    for i in range(N):
        dfs(i, 0, k)
    
    # print(dp)
    # get max
    res = 0
    for i in range(N):
        res = max(res, dp[i][0])
    # print(res)
    # go back to find path
    index = 0
    while res > 0:
        res -= 1
        for i in range(index+1, N):
            if dp[i][0] >= res:
                memo[index] = grid[i][0]
                index = i
                break
        for j in range(index+1, N):
            if dp[index][j] >= res:
                memo[index] = grid[index][j]
                index = j
                break
        # print(res,

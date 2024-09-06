
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
    n = len(grid)
    # 初始化dp矩阵，dp[i][j]表示走到(i,j)处最短路径的值
    dp = [[float('inf') for i in range(n)] for j in range(n)]
    dp[0][0] = grid[0][0]
    # 遍历每一条边
    for i in range(n):
        for j in range(n):
            # 边已经在dp矩阵中，则跳过
            if dp[i][j] == float('inf'):
                continue
            # 边的四个方向不在矩阵中，则跳过
            if i == 0 and j == 0:
                continue
            if i == 0 and j > 0:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i][j])
            if i > 0 and j == 0:
                dp[i - 1][j] = min(dp[i - 1][j], dp[i][j])
            if i > 0 and j > 0:
                dp[i - 1][j] = min(dp[i - 1][j], dp[i][j])
                dp[i][j - 1] = min(dp[i][j - 1], dp[i][j])
    # 对最后一个dp元素减去k，如果小于0则置为0
    return dp[n - 1][n - 1] - k

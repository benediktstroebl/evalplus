
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
    # ========================
    # DP方法
    # 从右上角开始计算，每一行计算之后再计算下一行
    # 
    # DP[i][j]：第i行j列 各个格子经过的数字总和最小值
    # ========================
    n = len(grid)
    m = len(grid[0])

    # DP[i][j] 代表每个格子经过的数字总和最小值
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # 最后一行的计算
    for j in range(m):
        dp[n-1][j] = grid[n-1][j]

    # 从下往上计算
    for i in range(n-2, -1, -1):
        for j in range(m):
            dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    
    # 求和最小值的数组
    ret = []

    # 求和最小值的数组
    for i in range(k-1, -1, -1):
        # 从最后一行开始往左上往上遍历
        # 找到一个最小值
        if i == k-1:
            ret.append(dp[0][0])
            continue

        min_sum = dp[0][0]
        for j in range(m):
            # 找到最小值
            if min_sum > dp[0][j]:
                min_sum = dp[0][j]

        ret.append(min_sum)

    return ret


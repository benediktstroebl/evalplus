
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
    # 简单dp问题，维护一个dp数组，依次添加当前最小的值
    N = len(grid)
    # 由于只有一行，或一列，或一个角，可以不用每次找最小值
    # 直接把所有可能的最小值全部计算出来即可
    res = []
    dp = [0] * (k + 1)
    dp[0] = grid[0][0]
    dp[1] = grid[0][1]
    dp[2] = grid[1][0]
    for i in range(2, k):
        dp[i + 1] = min(dp[i - 2], dp[i - 1], dp[i]) + grid[i // N][i % N]
    res.append(dp[k])
    for i in range(k - 1, 0, -1):
        if dp[i - 2] < dp[i - 1] and dp[i - 2] < dp[i]:
            res.append(grid[0][0])
        elif dp[i - 1] < dp[i - 2] and dp[i - 1] < dp[i]:
            res.append(grid[0][1])
        else:
            res.append(grid[1][0])
    return res[::-1]

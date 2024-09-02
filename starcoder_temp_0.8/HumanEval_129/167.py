
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
    # 动态规划
    # 设f(i, j, k)为从(i, j)出发，走到(i + 1, j + 1)需要走k步，且此路经经过的点所包含的数字最小值，
    # 则f(i, j, k) = min{f(i, j + 1, k - 1), f(i + 1, j, k - 1), f(i + 1, j + 1, k)}.
    # 其中f(i, j + 1, k - 1)表示在从(i, j)出发时，走到(i, j + 1)需要走k-1步的最小值，
    # f(i + 1, j, k - 1)表示在从(i, j)出发时，走到(i + 1, j)需要走k-1步的最小值，
    # f(i + 1, j + 1, k)表示在从(i, j)出发时，走到(i + 1, j + 1)需要走k步的最小值。
    # 复杂度分析
    # 设M为grid的行数，N为grid的列数，时间复杂度为O(M * N * K)。
    # 空间复杂度为O(M * N * K)。
    # 解法的解题思路和[79. Word Search]解法的思路相同，即逆向思维。
    # 考虑到要遍历grid中的所有点，可以将问题转换为求解从每个点出发，走到(M - 1, N - 1)时的最小值，
    # 即f(i, j, k) = min{f(i, j + 1, k - 1), f(i + 1, j, k - 1), f(i + 1, j + 1, k)}.
    # 由于grid中的每个点只可能出发到(M - 1, N - 1)或(M, N - 1)或(M - 1, N)三个点，
    # 因此用一个三维数组dp[M][N][k]来表示每个

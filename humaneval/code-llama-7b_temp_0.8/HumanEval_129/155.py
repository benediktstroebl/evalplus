
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
    m = len(grid[0])
    k = min(k, n*m)
    values = set()
    for i in range(n):
        for j in range(m):
            values.add(grid[i][j])
    values = list(values)
    values.sort()
    if len(values) <= k:
        return values

    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = 0

    for i in range(k):
        for j in range(n):
            for k in range(m):
                if grid[j][k] > i + 1:
                    continue
                if j - 1 >= 0:
                    dp[j][k] = min(dp[j][k], dp[j-1][k])
                if k - 1 >= 0:
                    dp[j][k] = min(dp[j][k], dp[j][k-1])
                if j + 1 < n:
                    dp[j][k] = min(dp[j][k], dp[j+1][k])
                if k + 1 < m:
                    dp[j][k] = min(dp[j][k], dp[j][k+1])
                dp[j][k] += grid[j][k]

    ans = []
    j, k = n - 1, m - 1
    while j >= 0 and k >= 0:
        if j - 1 >= 0 and dp[j][k] == dp[j - 1][k]:
            j -= 1
        elif k - 1 >= 0 and dp[j][k] == dp[j][k - 1]:
            k -= 1
        elif j + 1 < n and dp[j][k] == dp[j + 1][k]:
            j += 1
        elif k + 1 < m and dp[j][k] == dp[j][k + 1]:
            k

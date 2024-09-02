
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
    # edge case
    if not grid or k < 1 or not grid[0]:
        return None

    m, n = len(grid), len(grid[0])
    f = [[sys.maxsize] * (k + 1) for i in range(m + 1)]
    f[1][0] = 0
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if j - 1 >= 0 and grid[i][j - 1] < grid[i][j]:
                f[i + 1][j] = min(f[i][j - 1], f[i][j]) + grid[i][j]
            if i - 1 >= 0 and grid[i - 1][j] < grid[i][j]:
                f[i][j + 1] = min(f[i - 1][j], f[i][j]) + grid[i][j]
    r = []
    i = m
    j = k
    while i > 0 and j > 0:
        # UP
        if i - 1 >= 0 and f[i][j] - f[i - 1][j] == f[i - 1][j] - grid[i - 1][j]:
            i = i - 1
        else:
            r.append(grid[i - 1][j])
            j -= 1
        # LEFT
        if j - 1 >= 0 and f[i][j] - f[i][j - 1] == f[i][j - 1] - grid[i][j - 1]:
            j = j - 1
        else:
            r.append(grid[i][j - 1])
            i -= 1

    if j > 0:
        r.append(grid[i][j - 1])
    return r[::-1]


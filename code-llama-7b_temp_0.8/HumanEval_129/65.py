
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
    ans = []
    n = len(grid)
    rows = [ [0] * n for i in range(n) ]
    cols = [ [0] * n for i in range(n) ]
    rows[0][0] = grid[0][0]
    cols[0][0] = grid[0][0]
    for i in range(1, n):
        rows[i][0] = rows[i-1][0] + grid[i][0]
        cols[0][i] = cols[0][i-1] + grid[0][i]
    for i in range(1, n):
        for j in range(1, n):
            rows[i][j] = min(rows[i-1][j], cols[i][j-1]) + grid[i][j]
            cols[i][j] = min(rows[i][j], cols[i][j-1]) + grid[i][j]
    i, j = n-1, n-1
    ans.append(rows[i][j])
    while i > 0 and j > 0:
        if rows[i][j] == rows[i-1][j] or cols[i][j] == cols[i][j-1]:
            i -= 1
        elif rows[i][j] == cols[i-1][j] or cols[i][j] == rows[i][j-1]:
            j -= 1
        else:
            i -= 1
            j -= 1
        ans.append(grid[i][j])
    return ans[::-1]


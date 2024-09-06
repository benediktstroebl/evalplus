
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
    N = len(grid)
    if N == 0 and k == 0:
        return []

    def nbk(i, j, k):
        if k == 0:
            return True

        if len(grid) == i or len(grid[i]) == j:
            return False

        if grid[i][j] <= k:
            return nbk(i, j + 1, k - grid[i][j]) or nbk(i, j - 1, k - grid[i][j]) or nbk(i + 1, j, k - grid[i][j]) or nbk(i - 1, j, k - grid[i][j])

        return False

    def findPath(grid, k):
        N = len(grid)

        if N == 0 and k == 0:
            return []

        if N == 1 and k == 1:
            return [grid[0][0]]

        if len(grid) == 1 and len(grid[0]) == 1:
            return [grid[0][0]]

        # find the min path in each row
        M_matrix = []
        for i in range(N):
            M_matrix.append([N + 1] * N)
            M_matrix[i][0] = i + 1

        for j in range(1, N):
            for i in range(N - j):
                M_matrix[i][j] = min(M_matrix[i + 1][j - 1], M_matrix[i][j - 1], M_matrix[i + 1][j]) + 1

        # find the min path in each col
        N_matrix = []
        for j in range(N):
            N_matrix.append([N + 1] * N)
            N_matrix[j][0] = j + 1

        for i in range(1, N):
            for j in range(N - i):
                N_matrix[j][i] = min(N_matrix[j + 1][i - 1], N_matrix[j][i - 1], N_matrix[j + 1][i]) + 1

        # find
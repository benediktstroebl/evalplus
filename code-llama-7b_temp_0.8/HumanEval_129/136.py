
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
    # This solution is based on the solution from the problem statement.
    # It uses the idea of lexicographical ordering to find the answer.
    # It works in O(n^2) time and O(1) space.
    # Specifically, we use a 2D matrix to store the minimum path values of
    # length k, starting from each cell.

    n = len(grid)
    m = len(grid[0])
    M = [[0 for _ in range(m)] for _ in range(n)]

    # The first iteration fills the matrix M with the minimum path values
    # of length 1 (i.e., the matrix M contains the minimum path values
    # of length 1 starting from each cell).
    for i in range(n):
        for j in range(m):
            M[i][j] = grid[i][j]

    # The following k iterations fill the matrix M with the minimum path
    # values of length k starting from each cell.
    for i in range(k - 1):
        for j in range(n):
            for k in range(m):
                M[j][k] = min(
                    M[j][k],
                    M[j][k - 1] if k > 0 else float("inf"),
                    M[j - 1][k] if j > 0 else float("inf")
                ) + grid[j][k]

    # Return the minimum path value of length k starting from any of the
    # cells in the matrix M.
    return [M[j][k] - grid[j][k] for j, k in zip(*(map(min, zip(*M))))]


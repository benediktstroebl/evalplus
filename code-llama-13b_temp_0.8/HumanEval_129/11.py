
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
    # Helper method to find minimum sum path
    def minPath(r, c, k, grid, res):
        # If k is 0 or we are out of grid return
        if k == 0 or r < 0 or c < 0:
            return
        # If k is 1, we have reached minimum path
        if k == 1:
            res.append(grid[r][c])
            return
        # Recursively find minimum path
        minPath(r-1, c, k-1, grid, res)
        minPath(r, c-1, k-1, grid, res)

    # Initialization
    n = len(grid)
    # Find minimum sum path
    res = []
    minPath(n-1, n-1, k, grid, res)
    return res



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
    # Optimization:
    # Most people think the grid is a list of lists of integers, but it's
    # actually a list of tuples.
    grid = list(map(tuple, grid))

    # For each point (x, y) in the grid, you can now consider the rows
    # up to (x, y) and the columns up to (x, y).
    # We now compute the number of paths if we take one of the rows or one of
    # the columns, that is, we choose the column or row that is smaller.
    # Each cell stores the maximum value we can obtain by taking one of the
    # above paths, and then the minimum value we can obtain by taking the
    # maximum of the paths we choose from the cell above.
    # We compute this value as the minimum of the two paths.
    # (Note that we can't do computations without taking the paths, since
    # the number of cells must be the same.)
    #
    # For each cell (x, y), we compute the total number of paths that we can
    # take from the cell above that we can build the row up to (x, y) and then
    # the column up to (x, y).
    #
    # dp[x][y] represents the maximum number of paths that we can take from the
    # cell above that we can build the row up to (x, y) and then the column up
    # to (x, y).
    #
    # We compute the total number of paths from the cell above that we can
    # build the row up to (x, y) using dp[x - 1][y].
    #
    # We compute the total number of paths from the cell above that we can
    # build the column up to (x, y) using dp[x][y - 1].
    #
    # Every cell (x, y) in the grid contains two values: dp[x][y] and
    # grid[x][y].
    # If dp[x][y] = dp[x - 1][y] + grid[x][y], that means we can build the row
    # up to (x, y) from the cell above and the column up
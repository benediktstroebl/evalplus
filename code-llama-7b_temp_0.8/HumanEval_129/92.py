
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

    if not grid: return []
    
    m = len(grid)
    n = len(grid[0])

    # OPTIMIZATION 1
    # Optimize on the input parameters, i.e. the given grid
    # Since we know that all the integers in the range [1, N * N] inclusive
    # appear exactly once on the cells of the grid, it is possible to build
    # a histogram of the integers which shows how many times they appear.
    # Thus, the histogram will contain exactly N * N buckets, one for each
    # integer in the range [1, N * N] inclusive. The sum of the values of 
    # the buckets must be N * N. The sum of the values of the buckets that
    # correspond to the integers that appear on the cells of the grid must
    # be equal to the sum of the values of the buckets that correspond to the
    # integers that do NOT appear on the cells of the grid. In other words,
    # the sum of the values of the buckets that correspond to the integers
    # that appear on the cells of the grid is equal to N * N - M, where M is
    # the number of integers that appear on the cells of the grid. Since
    # each bucket contains at most one integer, the value of each bucket
    # must be either 0 (the integers that do NOT appear on the cells of the
    # grid) or 1 (the integers that appear on the cells of the grid). This
    # optimization uses an array of size N * N to store the histogram.
    #
    # OPTIMIZATION 2
    # Optimize on the actual problem that we want to solve, i.e. find the
    # minimum path of length k. To solve this problem, we don't actually need
    # to store a histogram, since all the information that we need is already
    # contained in the grid. 
    #
    # Thus, we can create a table of size (M + 1) * M, where M is the number
    # of integers that appear on the cells of the grid. The table will
    # contain exactly M * M buckets, one for each possible value of the

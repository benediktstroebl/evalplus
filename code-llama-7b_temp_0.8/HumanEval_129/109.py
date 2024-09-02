
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

    ###############################
    # SOLUTION
    ###############################
    # The grid is a 2D array, so to make it a 1D array, we need to convert
    # the second dimension into the elements of the 1D array.
    #
    # For example, if the grid is:
    #   1 2 3
    #   4 5 6
    #   7 8 9
    #
    # Then the 1D array will be:
    #   [1, 4, 7, 2, 5, 8, 3, 6, 9]
    #
    # In this case, we will look for the minimum path of length 3 (k) in the 1D array.
    # The minimum path will have three elements. So, we will need to select
    # three distinct elements from the 1D array.
    # The three elements must have an increasing order, since they form a path.
    # The elements of the minimum path must be:
    # 1 <= elem1 <= elem2 <= elem3
    #
    # So, after we get the minimum path, we need to go back to the 2D array and
    # find the elements.

    # O(k*n*n) time | O(n*n) space - where n is the number of rows in the grid
    # and k is the length of the path.

    # This problem is similar to the subset sum problem.
    # We can use dynamic programming to solve it.
    # Let's start with a basic grid like this:
    #   [ 5 9 3 ]
    #   [ 4 1 6 ]
    #   [ 7 8 2 ]
    #
    # At every step, we can either move up or right to get to the next number.
    #
    # In the first step, we can get to:
    #   [ 1 9 3 ]
    #   [ 4 5 6 ]
    #   [ 7 8 2 ]
    #
    # In the second step, we can get to:
    #   [ 1 2 3 ]

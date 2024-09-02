
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

    # the minimum path in each cell of the grid
    # we can modify this grid in place
    # we can also save the minimum path in each cell 
    # by having 2d array of size (N + 1) * (N + 1) 
    # where each cell is an array of length k 
    # the first cell will be an array of length 1 
    # and the last cell will be an array of length k 
    # in every other cell we will have a number of path that goes through the cell
    # and the minimum path is the one with the minimum value in that array
    # since we are allowed to go to any of the neighboors
    # this means we are not limited by the direction of the path
    # so in each cell we have a list of paths
    # the list will have a path for every cell that is reachable from this cell
    # the path will be ordered
    # we can go to a cell and then back to the current cell
    # this will give us a path of length 2 * k
    # in the example in the problem statement
    # for the cell [5, 9, 3] we can start from [5, 9, 3] or [5, 9, 4] or [5, 9, 5]
    # and the path will be [5, 9, 3, 4, 5]
    # the path [5, 9, 4, 5, 6] is not a valid path since it starts from [5, 9, 3]
    # and ends at [5, 9, 4] and [5, 9, 5]
    # so the path [5, 9, 3, 4, 5] is the minimum path from [5, 9, 3]
    # the path [5, 9, 4, 5, 6] is not a valid path
    # but we can start from any cell of the grid and end at any cell of the grid
    # so every cell has a list of paths
    # now the question is how do we find the minimum path
    # we can use the fact that we can only go to a cell that is reachable from the current cell
    # so for the cell [5, 9, 3] the list of paths is [ [5, 9, 3


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
    # we need to find a path of length k
    # we can go from any cell to any other cell by crossing an edge (no diagonals)
    # so, this is a directed graph
    # once we know which cells we have visited, we can go from those cells
    # to any other cell by crossing an edge
    # so, this is a graph of paths
    # we want the lexicographically minimal path
    # this means that we want the minimal distance between any two cells
    # that form a path
    # we can do a dfs for every cell, but we will need to keep track of all paths
    # and their lengths
    # we can start with the cell that has the smallest integer value
    # we can then build a dictionary of the paths that we have found
    # we can then find the minimal distance for every pair of cells
    # we can then find the minimal path that connects all the cells
    # we can then return the path

    # dictionary of all paths
    paths = {}
    # length of the path
    path_len = 0
    # start from the cell with the smallest

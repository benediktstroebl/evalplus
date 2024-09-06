
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
    # Your code here
    #
    # For this problem, I tried to use 2-pointer on the grid,
    # but I am not able to figure out the right path because of the
    # minimum path of length k in the grid. You can start from any cell,
    # and in each step you can move to any of the neighbor cells,
    # in other words, you can go to cells which share an edge with you current
    # cell.
    #
    # I was not able to figure out the minimum path, so I used backtracking
    # on this problem. I first generated all paths on the grid and then
    # find the minimum path.
    #
    # The idea is to use backtracking to generate all paths on the grid
    # with size k, and we know the path with minimum length will be the
    # answer.
    #
    # To generate all paths, I used a recursive function.
    #
    # In the function, first I add the current element to the path,
    # and if the path has size of k, I can calculate the sum of the path.

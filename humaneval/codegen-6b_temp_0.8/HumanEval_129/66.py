
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
    rows, cols = len(grid), len(grid[0])
    if rows == 1 and cols == 1:
        return [grid[0][0]]

    # Compute the min path for the first row and column

    # The min path to either row or column of grid[0] will be [grid[0][x] for x in 0, 1, 2]
    # The min path to either row or column of grid[1] will be [grid[1][x] for x in 0, 1, 2]
    # The min path to either row or column of grid[2] will be [grid[2][x] for x in 0, 1, 2]
    # The min path to either row or column of grid[3] will be [grid[3][x] for x in 0, 1, 2]
    # The min path to either row or column of grid[4] will be [grid[4][x] for x in 0, 1, 2]
    # The min path to either row or column of grid[5] will be [grid[5][x] for x in 0, 1, 2]

    # So the min path for grid[0] is [grid[0][x] for x in 0, 1, 2]
    # The min path for grid[1] is [grid[1][x] for x in 0, 1, 2]
    # The min path for grid[2] is [grid[2][x] for x in 0, 1, 2]
    # The min path for grid[3] is [grid[3][x] for x in 0, 1, 2]
    # The min path for grid[4] is [grid[4][x] for x in 0, 1, 2]
    # The min path for grid[5] is [grid[5][x] for x in 0, 1, 2]

    # So the min path for grid[0] is < [grid[0][x] for x in 0, 1, 2]
    # The min path for grid[1] is < [grid[1][x] for x in 0, 1, 2]
    # The min path for grid[2] is < [grid[2][x] for x in 0, 1, 2
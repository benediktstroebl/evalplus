
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
    # If there is no need to visit any more cells, the current solution is optimal
    if k <= 0:
        return []
    # If the minimum path is on the left edge, the solution is to go left
    if k == grid[0][0]:
        return [grid[0][0]]
    # If the minimum path is on the bottom edge, the solution is to go down
    if k == grid[-1][-1]:
        return [grid[-1][-1]]
    # If the minimum path is on the top edge, the solution is to go up
    if k == grid[0][-1]:
        return [grid[0][-1]]
    # If the minimum path is on the right edge, the solution is to go right
    if k == grid[-1][0]:
        return [grid[-1][0]]
    # If we are at the top left corner, the solution is to go up and left
    if k == grid[0][0]:
        return [grid[0][0]]
    # If we are at the top right corner, the solution is to go up and right
    if k == grid[0][-1]:
        return [grid[0][-1]]
    # If we are at the bottom left corner, the solution is to go down and left
    if k == grid[-1][0]:
        return [grid[-1][0]]
    # If we are at the bottom right corner, the solution is to go down and right
    if k == grid[-1][-1]:
        return [grid[-1][-1]]

    # if k > 0
    if k >= grid[0][0]:
        # Go down-left
        down_left = minPath(grid[1:], k - grid[0][0])
        # Go up-left
        up_left = minPath(grid[:-1], k - grid[0][0])
        if down_left[-1] < up_left[-1]:
            return [grid[0][0]] + down_left
        else:
            return [grid[0][0]] + up_left
    # if k < 0
    elif k < grid[-1][-1]:
        # Go

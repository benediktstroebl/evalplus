
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
    if not grid or not grid[0]:
        raise ValueError("grid must be 2D array of size >= 2x2")

    rows, cols = len(grid), len(grid[0])
    if rows < 2 or cols < 2:
        raise ValueError("grid must be 2D array of size >= 2x2")

    if k < 1 or k > rows * cols:
        raise ValueError("k must be >= 1 and <= N*N")

    # create an ordered list of each value
    # 1st value = 1, 2nd value = 2, 3rd value = 3 ... N*Nth value = N*N
    value_list = list(range(1, rows * cols + 1))

    # find the value of cell[0][0]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == value_list[0]:
                return findPath(grid, value_list, 0, 0, k)


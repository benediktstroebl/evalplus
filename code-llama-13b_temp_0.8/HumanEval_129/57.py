
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

    # Current row and column indices
    row = 0
    col = 0

    # Nested list row_distances keeps the distance of each number in the
    # current row from the start. This way, we can quickly get the
    # distances of any number from the start when moving to the next row.
    #
    # row_distances = [
    #   [0, 0, 0, 0],
    #   [0, 1, 2, 1],
    #   [0, 2, 4, 2],
    #   [0, 3, 6, 3],
    #   [0, 4, 8, 4]
    # ]
    row_distances = [[0] * len(grid) for _ in range(len(grid))]
    for col in range(len(grid)):
        row_distances[0][col] = col

    # Nested list col_distances keeps the distance of each number in the
    # current column from the start. This way, we can quickly get the
    # distances of any number from the start when moving to the next column.
    #
    # col_distances = [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [1, 1, 1, 1, 1],
    #   [2, 2, 2, 2, 2],
    #   [3, 3, 3, 3, 3]
    # ]
    col_distances = [[0] + [row for row in range(len(grid) - 1)]
                     for _ in range(len(grid))]

    # The last element of the min_path will be the path of smallest length
    min_path = [[] for _ in range(k)]

    # Iterate over each number in grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # Skip the current number if it's not k
            if grid[row][col

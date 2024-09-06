
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
    # Setup
    row = len(grid)
    col = len(grid[0])

    # Paths will contain the path of each grid cell
    # Paths[row][col][k] is the kth shortest path
    # from the top left to the cell at row, col
    paths = [[[None for _ in range(k+1)] for _ in range(col+1)] for _ in range(row+1)]

    # Base Case: The shortest path to a single cell is an edge
    for i in range(row+1):
        for j in range(col+1):
            if i == 0 and j == 0:
                paths[i][j][0] = []
            elif i == 0 or j == 0:
                paths[i][j][0] = [grid[i-1][j-1]]

    # General Case: The shortest path to a cell is either
    # the shortest path to the cell immediately above it plus
    # an edge or the shortest path to the cell immediately
    # to the left of it plus an edge
    for i in range(1, row+1):
        for j in range(1, col+1):
            # Calculate the shortest paths to the cells above and left of
            # the current cell
            top_path = paths[i-1][j][0]
            left_path = paths[i][j-1][0]

            # The shortest path to the current cell is whichever of the two is
            # the shortest plus the current cell
            paths[i][j][0] = (
                top_path if len(top_path) <= len(left_path) else left_path
            ) + [grid[i-1][j-1]]

            # Calculate all paths of length >= 2 up to k
            for l in range(1, k+1):
                # Store the shortest path of length l found so far
                # in the variable min_path
                min_path = None
                # Calculate the shortest path to the current cell
                # by going from the cell immediately above or to
                # the left of it and adding the

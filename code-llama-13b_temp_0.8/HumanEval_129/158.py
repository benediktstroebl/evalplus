
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
    # get dimensions of grid
    N = len(grid)

    # construct a state where the value at the top is the minimum path to
    # the top of the grid, and the value at (i, j) is the minimum path to the
    # grid cell at (i, j)
    states = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        states[0][i] = 1 + i

    # fill in the states
    for i in range(1, N):
        for j in range(N):
            left = states[i-1][j]
            top = states[i][j-1]
            states[i][j] = min(left, top) + 1

    # backtrack to find the best path
    best_path = []
    i = N - 1
    j = N - 1
    while i > 0 or j > 0:
        best_path.insert(0, grid[i][j])
        # from current cell, find the next cell to move to
        left = states[i-1][j]
        top = states[i][j-1]
        if left < top:
            i -= 1
        else:
            j -= 1

    return best_path


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
    N = len(grid)
    # Base Case: The shortest row/column will always be of length k
    if k in (N, N - 1):
        return grid[0][:k]

    lst_min = []
    for r in range(N):
        # set row
        # initialize to length of k
        lst_min.append(k)
        for c in range(N - 1, r, -1):
            # start from the end of the row
            if lst_min[r] == k:
                # if the cell is all zeros, meaning that the actual kth cell
                # is the only one
                if grid[r][c] == 0:
                    # clear out the min value on cells in the row above it
                    for var in lst_min[:r]:
                        lst_min[var] = 0
                    lst_min[r] = 0
                else:
                    # get the min value without making the kth cell -1
                    # because the grid is all zero
                    lst_min[r] -= 1

    for c in range(N):
        # set column
        # initialize to length of k
        for r in range(N - 1, c, -1):
            if lst_min[r] == k:
                # if the cell is all zeros, meaning that the actual kth cell
                # is the only one
                if grid[r][c] == 0:
                    # clear out the min value on cells in the column above it
                    for var in lst_min[:c]:
                        lst_min[var] = 0
                    lst_min[c] = 0
                else:
                    # get the min value without making the kth cell -1
                    # because the grid is all zero
                    lst_min[c] -= 1

    for r in range(N):
        for c in range(N):
            # get the min value on the kth cell
            if r == c:
                lst_min[r] = grid[r][c]
            elif r < c:
                lst_min[r] = min(lst_min[r], lst_
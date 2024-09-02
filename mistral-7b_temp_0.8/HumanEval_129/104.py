
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
    m, n = len(grid), len(grid[0])
    i, j = 0, 0
    min_path = []

    while i < m and j < n:
        # if we haven't filled in the k cells, keep checking
        if len(min_path) < k:
            # check if it is valid to go to a neighboring cell, i.e.,
            # if the current cell is in the path of the neighboring cell
            if i + 1 < m and grid[i + 1][j] in min_path:
                # go to the next cell
                i += 1
            elif j + 1 < n and grid[i][j + 1] in min_path:
                # go to the next cell
                j += 1
            # if we've filled in the k cells and we haven't reached the end of
            # the grid, go to the next cell
            else:
                min_path.append(grid[i][j])
                if i + 1 < m:
                    i +=

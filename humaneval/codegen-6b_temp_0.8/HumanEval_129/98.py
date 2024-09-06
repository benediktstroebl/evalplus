
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
    if (m < 2 or n < 2) or (k < 0):
        return []
    if k == 0:
        return []
    if k == 1:
        return grid[0]
    if k == 2:
        return [min(grid[0][0], grid[0][1]),
                min(grid[1][0], grid[1][1])]
    total_path = []
    # row_path is the list of minimum path at each row
    row_path = [None] * n
    # Initialize the path with the first row of the grid
    for i in range(n):
        row_path[i] = [grid[0][i]]
    total_path = row_path[:]
    # compute the min path from rows
    for i in range(1, m):
        row_path = [None] * n
        for j in range(n):
            # initialize the next level to the len of current level
            curr_level = [grid[i][j]] * (len(row_path) + 1)
            # compute the min of the current level and the current row
            for k in range(1, len(row_path)):
                curr_level[k] = min(row_path[k - 1] + [grid[i][j]],
                                    row_path[k] + [grid[i][j]])
            # store the min of the next level
            row_path = curr_level
        # append the path at the current row
        total_path += row_path
    # find the min path from the last row, excluding the last element
    total_path.pop()
    # return the last element
    return total_path[-1]


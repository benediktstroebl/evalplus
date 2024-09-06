
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
    min_path = []
    row_count = len(grid)
    column_count = len(grid[0])

    if k > row_count * column_count:
        raise Exception("K can not be greater than total count of cells")

    if k < 0:
        raise Exception("K can not be negative")

    def find_min_path(row, column, k):
        nonlocal min_path
        if k == 0:
            return True
        if column < 0 or column >= column_count:
            return False
        if row < 0 or row >= row_count:
            return False
        if (row, column) in min_path:
            return False
        if grid[row][column] > k:
            return False

        min_path.append((row, column))

        if find_min_path(row + 1, column, k - grid[row][column]):
            return True
        if find_min_path(row - 1, column, k - grid[row][column]):
            return True
        if find_min_path(row, column + 1, k - grid[row][column]):
            return True
        if find_min_path(row, column - 1, k - grid[row][column]):
            return True

        return False

    find_min_path(0, 0, k)
    min_path.sort()
    return [grid[x][y] for x, y in min_path]


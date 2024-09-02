
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
    shp = grid.shape
    assert len(shp) == 2
    assert shp[0] > 0 and shp[1] > 0
    assert isinstance(k, int) and k > 0
    
    def get_coordinates(row, col):
        assert isinstance(row, int) and row > 0
        assert isinstance(col, int) and col > 0
        return (row, col)

    def get_neighbors(coord):
        row, col = coord
        if row > 0:
            yield get_coordinates(row - 1, col)
        if row < shp[0] - 1:
            yield get_coordinates(row + 1, col)
        if col > 0:
            yield get_coordinates(row, col - 1)
        if col < shp[1] - 1:
            yield get_coordinates(row, col + 1)
    
    def row_order_and_value(row, col, curr_values):
        # if there are still not enough values, return
        if row == shp[0] - 1:
            return
        # if there are no values left, recurse
        if 0 == len(curr_values):
            row_order_and_value(row + 1, col, [grid[row + 1][col]])
        # otherwise, compare the current and next row value, and recurse
        else:
            next_row = row + 1
            next_col = col
            if 0 == next_col:
                next_col = shp[1] - 1
            if grid[next_row][next_col] < grid[row][col]:
                row_order_and_value(row + 1, col, list(curr_values) + [grid[next_row][next_col]])
            else:
                row_order_and_value(row + 1, col, list(curr_values))

    def min_path_helper(row, col, curr_values):
        if len(curr_values) == k:
            return curr_values
        # get the coordinates of the next values to explore
        next
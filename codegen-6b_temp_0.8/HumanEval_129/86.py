
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

    def get_top_left_cell(row, col):
        return (row - 1, col - 1)

    def get_top_cell(row, col):
        return (row - 1, col)

    def get_top_right_cell(row, col):
        return (row - 1, col + 1)

    def get_right_cell(row, col):
        return (row, col + 1)

    def get_bottom_right_cell(row, col):
        return (row + 1, col + 1)

    def get_bottom_cell(row, col):
        return (row + 1, col)

    def get_bottom_left_cell(row, col):
        return (row + 1, col - 1)

    def get_left_cell(row, col):
        return (row, col - 1)

    def get_cell_value_in_direction(row, col, direction):
        if direction == LEFT:
            return grid[row][col - 1]
        elif direction == RIGHT:
            return grid[row][col + 1]
        elif direction == TOP:
            return grid[row - 1][col]
        elif direction == BOTTOM:
            return grid[row + 1][col]
        elif direction == TOP_LEFT:
            return grid[row - 1][col - 1]
        elif direction == TOP_RIGHT:
            return grid[row - 1][col + 1]
        elif direction == BOTTOM_LEFT:
            return grid[row + 1][col - 1]
        elif direction == BOTTOM_RIGHT:
            return grid[row + 1][col + 1]

    def get_direction_of_smaller_path(current_row, current_col, direction):
        top_left = get_top_left_cell(current_row, current_col)
        top = get_top_cell(current_row, current_col)
        top_right = get_top_right_cell(current_row, current_col)
        right = get_right_cell(current_row, current_col)
        bottom_
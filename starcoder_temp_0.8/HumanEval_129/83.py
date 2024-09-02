
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
    def find_next_cell(curr, k):
        next_cell = None
        if curr[0] > 0:
            next_cell = (curr[0] - 1, curr[1])
        elif curr[1] > 0:
            next_cell = (curr[0], curr[1] - 1)
        if next_cell is None:
            return None
        if k == 1:
            return [grid[next_cell[0]][next_cell[1]]]
        return find_next_cell(next_cell, k - 1) + [grid[next_cell[0]][next_cell[1]]]

    def min_path_from_cell(start, k):
        if k == 1:
            return grid[start[0]][start[1]]
        next_cells = find_next_cell(start, k - 1)
        if next_cells is None:
            return None
        return min(min_path_from_cell(cell, k - 1) for cell in next_cells)

    if k > min(len(grid), len(grid[0])):
        return None
    min_row = min_path_from_cell((0, 0), k)
    min_col = min_path_from_cell((0, 0), k)
    min_path = [grid[0][0]]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            min_path.append(grid[row][col])
            if row == 0 and col == 0:
                continue
            if row == 0:
                min_path.append(min_col)
            if col == 0:
                min_path.append(min_row)
    return min_path

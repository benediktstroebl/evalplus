
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
    result = []
    min_value = 1
    max_value = grid[0][0]
    for row in grid:
        for value in row:
            if value < min_value:
                min_value = value
            elif value > max_value:
                max_value = value
    if k > len(grid)*len(grid[0]):
        return []
    if k == 1:
        return [min_value]
    if k == len(grid)*len(grid[0]):
        return [i for row in grid for i in row]
    if k < min_value:
        return []
    if k >= max_value:
        for row in grid:
            for value in row:
                if value == max_value:
                    result.append(value)
        return result

    def get_neighbors(row, col, value):
        """
        Given a value, determine the cells that this value should go through.
        """
        result = []
        if row > 0:
            result.append((row-1, col, grid[row-1][col]))
        if row < len(grid)-1:
            result.append((row+1, col, grid[row+1][col]))
        if col > 0:
            result.append((row, col-1, grid[row][col-1]))
        if col < len(grid[0])-1:
            result.append((row, col+1, grid[row][col+1]))
        return result

    result = []
    cell_queue = []
    for row, col in product(range(len(grid)), range(len(grid[0]))):
        value = grid[row][col]
        if value == k:
            result.append(k)
            break
        if value == min_value:
            cell_queue.append((row, col, value))
    while cell_queue:
        row, col, value = cell_queue.pop(0)
        k -= 1
        result.append(value)
        for next_row, next_col, next_value in get_neighbors(row,

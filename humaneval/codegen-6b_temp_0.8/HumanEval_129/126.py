
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
    row_len = len(grid)
    col_len = len(grid[0])
    
    visiting_order = []

    def find_min_path(row, col, visited_set, path):
        if (row, col) in visited_set:
            return
        visited_set.add((row, col))
        if len(path) == k:
            visiting_order.append(path)
            return
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for direction in directions:
            row_step, col_step = direction
            new_row, new_col = row + row_step, col + col_step
            if new_row >= 0 and new_row < row_len and new_col >= 0 and new_col < col_len:
                find_min_path(new_row, new_col, visited_set, path + [grid[new_row][new_col]])

    for row in range(row_len):
        for col in range(col_len):
            visited_set = set()
            find_min_path(row, col, visited_set, [grid[row][col]])
    
    return visiting_order[0]



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
    def backtrack(k, grid, row, col, grid_len, path):
        if row == row_num and col == col_num:
            path.append(grid[row_num][col_num])
            if k == len(path):
                return True

        if k > len(path):
            return False

        for i in range(4):
            x = row + direction[i][0]
            y = col + direction[i][1]

            if x >= 0 and x < row_num and y >= 0 and y < col_num:
                path.append(grid[x][y])
                if backtrack(k, grid, x, y, grid_len, path):
                    return True
                else:
                    path.pop()

        return False

    row_num = len(grid)
    col_num = len(grid[0])
    path = []

    for i in range(row_num):
        for j in range(col_num):
            if backtrack(k, grid, i

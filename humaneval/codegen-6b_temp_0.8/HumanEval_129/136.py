
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
    def dfs(row, col, visited, visited_set, cur, path, rows, cols, path_length):
        # base case
        if (row, col) in visited_set:
            return False

        if path_length == k:
            return True

        res = False

        for n_row, n_col in neigbours(row, col):
            if grid[n_row][n_col] not in cur:
                cur.add(grid[n_row][n_col])
                res = res or dfs(n_row, n_col, visited | {(row, col)}, visited_set | {(n_row, n_col)}, cur, path + [grid[n_row][n_col]], rows, cols, path_length + 1)
                res = res or dfs(n_row, n_col, visited, visited_set, cur - {grid[n_row][n_col]}, path + [grid[n_row][n_col]], rows, cols, path_length + 1)
                cur.discard(grid[n_row][n_col])

        return res

    def neigbours(row, col):
        if row > 0:
            yield (row - 1, col)
        if row < rows - 1:
            yield (row + 1, col)
        if col > 0:
            yield (row, col - 1)
        if col < cols - 1:
            yield (row, col + 1)

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, set(), set([]), set([grid[row][col]]), [], rows, cols, 0):
                return grid[row][col]


grid = [ [1,2,3], [4,5,6], [7,8,9] ]
k = 3
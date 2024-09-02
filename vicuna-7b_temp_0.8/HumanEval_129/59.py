
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
    if not grid:
        return []

    n = grid.n
    grid_list = sorted(grid)

    if n == 1:
        return grid_list

    m = grid.m
    min_path_list = []

    def dfs(row, col, path_list, path=None):
        global m, n
        if row < 0 or row >= n or col < 0 or col >= n:
            return

        if row == 0 and col == 0 and path_list:
            min_path = min(min_path_list, key=lambda x: grid_list[x])
            min_path_list = min_path
            return

        if grid_list[row][col] == 0:
            for i in range(grid_list[row][col], grid_list[row][col]+1):
                dfs(row+i, col, path_list, path)
        else:
            for i in range(grid_list[row][col], grid_list[row][col]+1):
                for j in range(grid_list[row][col], grid_list[row][col]+1):
                    if (row, col) == (0, 0) or (row-1, col) or (row, col+1) or (row+1, col) or (row, col+2) in path_list:
                        dfs(row, col, path_list, path + (row, col))

    dfs(0, 0, [], [])
    return min_path_list[0]
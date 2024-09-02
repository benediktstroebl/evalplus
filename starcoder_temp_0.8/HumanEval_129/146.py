
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

    # #Method 1
    # row = len(grid)
    # col = len(grid[0])
    # if k < 0 or row < k or col < k:
    #     return []
    # if k == 0 or row == 1 or col == 1:
    #     return grid[0][0]

    # path = [grid[0][0]]
    # for i in range(k):
    #     row_start = max(0, i - k + 1)
    #     row_end = min(row, i + k + 1)
    #     col_start = max(0, i - k + 1)
    #     col_end = min(col, i + k + 1)
    #     curr_row_min = path[-1]
    #     for i in range(row_start, row_end):
    #         curr_row_min = min(curr_row_min, grid[i][col_start:col_end + 1])
    #     path.append(curr_row_min)

    # return path

    #Method 2
    # row = len(grid)
    # col = len(grid[0])
    # if k < 0 or row < k or col < k:
    #     return []
    # if k == 0 or row == 1 or col == 1:
    #     return grid[0][0]
    # graph = [[float('inf') for _ in range(col)] for _ in range(row)]
    # graph[0][0] = grid[0][0]
    # for i in range(1, k + 1):
    #     row_start = max(0, i - k + 1)
    #     row_end = min(row, i + k + 1)
    #     col_start = max(0, i - k + 1)
    #     col_end = min(col, i + k + 1)
    #     for row in range(row_start, row_end):
    #         graph[row][col_start] = min(graph[row][col_start], grid[row][col_start])
    #         graph[row][col_end - 1] = min(graph[row][col_end - 1

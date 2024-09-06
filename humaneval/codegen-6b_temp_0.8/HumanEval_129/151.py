
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
    if not grid or not grid[0]:
        return []
    rows, cols = len(grid), len(grid[0])

    if k == 0:
        return []

    if k == 1:
        return [min(grid[i][j] for i in range(rows) for j in range(cols))]

    dist_map = [[[False for _ in range(cols)] for _ in range(rows)] for _ in
                range(k + 1)]
    dist_map[0] = [[True for _ in range(cols)] for _ in range(rows)]
    dist_map[1] = [
        [True if grid[i][j] == grid[0][0] else False for j in range(1, cols)]
        for i in range(len(grid))
    ]

    for row in range(rows):
        for col in range(cols):
            dist_map[0][row][col] = True

    for row in range(1, rows):
        for col in range(1, cols):
            dist_map[1][row][col] = grid[row][col] == grid[row - 1][col]

    for row in range(2, rows):
        for col in range(1, cols):
            for k in range(2, k + 1):
                dist_map[k][row][col] = grid[row][col] > grid[row - 1][col] \
                    and dist_map[k - 1][row - 1][col]

    result = [grid[0][0]]

    for row in range(1, rows):
        for col in range(1, cols):
            if dist_map[k][row][col]:
                result.append(grid[row][col])

    return result


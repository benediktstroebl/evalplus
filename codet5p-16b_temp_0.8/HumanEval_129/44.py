
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

    rows, cols = len(grid), len(grid[0])
    if rows <= 1 or cols <= 1: return []
    if k == 0: return []
    if k == 1: return [min(grid[0])]
    lst = []
    for i in range(rows):
        for j in range(cols):
            lst.append([i, j])
    lst.sort()
    curr = [0, 0]
    path = [[0 for _ in range(cols)] for _ in range(rows)]
    path[0][0] = lst[0]
    curr = path[0][0]
    vis = set()
    for i in range(1, k):
        next_step = []
        for v in lst:
            if v[0] == curr[0]:
                next_step.append([v[1], v[0]])
            if v[1] == curr[1]:
                next_step.append([v[1], v[1]])
            if v[0] > curr

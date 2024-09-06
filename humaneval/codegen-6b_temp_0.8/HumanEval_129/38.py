
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

    m, n = len(grid), len(grid[0])
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    # construct the sudoku
    costs = [[1e9] * n for _ in range(m)]

    def isValid(x, y):
        return x >= 0 and x < m and y >= 0 and y < n

    def solve(x, y, k):
        if k == 1:
            return
        for i, j in directions:
            if isValid(x + i, y + j) and \
                grid[x + i][y + j] <= m * n and \
                costs[x + i][y + j] + 1 < costs[x][y]:
                costs[x + i][y + j] = costs[x][y] + 1
                solve(x + i, y + j, k - 1)

    # search minimum length path from the boundary
    for i in range(m):
        costs[i][0] = 0
        solve(i, 0, k)
    for i in range(n):
        costs[0][i] = 0
        solve(0, i, k)
    
    res = []
    for i, j in directions:
        if isValid(0 + i, 0 + j) and \
            costs[0 + i][0 + j] <= k:
            res.append(grid[0 + i][0 + j])
    return res


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
    N = len(grid)
    if k < 1 or not grid or not N:
        return []

    k += 1
    m, n = N, N

    # convert a grid of rows into a grid of columns
    for i in xrange(m):
        grid[i] = grid[i] + [0] * (n - 1 - i)

    # initialize the grid
    grid = [GridCell(i, grid[i][j]) for i in xrange(m) for j in xrange(n)]

    # BFS
    q = collections.deque([])
    for i in xrange(m):
        for j in xrange(n):
            cell = grid[i*n + j]
            if cell.val == 1:
                q.append(cell)
                cell.dist = 0
                cell.prev = None

    while q:
        cell = q.popleft()
        i, j = cell.i, cell.j
        # check the top cell, the right cell, and the bottom cell
        if i > 0:
            top_cell = grid[(i - 1) * n + j]
            if top_cell.val < cell.val:
                top_cell.dist = cell.dist + 1
                top_cell.prev = cell
                q.append(top_cell)

        if j > 0:
            left_cell = grid[i * n + j - 1]
            if left_cell.val < cell.val:
                left_cell.dist = cell.dist + 1
                left_cell.prev = cell
                q.append(left_cell)

        if i < m - 1:
            bottom_cell = grid[(i + 1) * n + j]
            if bottom_cell.val < cell.val:
                bottom_cell.dist = cell.dist + 1
                bottom_cell.prev = cell
                q.append(bottom_cell)

        if j < n - 1:
            right_cell = grid[i * n + j + 1]
            if right_cell.val < cell.val:
                right_cell.dist = cell.dist + 1
                right_cell.prev

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
    # Returns true if it is possible to reach (x, y) from (sx, sy) in k steps
    def possible(x, y, sx, sy, k):
        if x < 0 or x >= N or y < 0 or y >= N or k < 0:
            return False
        if (sx, sy) == (x, y):
            return k == 0
        return grid[x][y] >= grid[sx][sy] and possible(
            x, y, sx, sy, k - 1
        )

    # Returns the lexicographically minimum path from (x, y) in k steps
    def getPath(x, y, k):
        if x < 0 or x >= N or y < 0 or y >= N or k < 0:
            return []
        if (x, y) in mem and mem[(x, y)] <= k:
            return paths[(x, y)]
        mem[(x, y)] = k
        result = []
        for i in range(N):
            for j in range(N):
                if possible(i, j, x, y, k):
                    path = getPath(i, j, k - 1)
                    if path:
                        result.append(path)
        if result:
            result.sort()
            paths[(x, y)] = result[0]
            return result[0]
        else:
            return []

    paths = {}
    mem = {}
    N = len(grid)
    (sx, sy) = (0, 0)
    min_k = 0
    for i in range(N):
        for j in range(N):
            k = getPath(i, j, grid[i][j])
            if k:
                if i == sx and j == sy:
                    min_k = grid[i][j]
                else:
                    if len(k) < min_k:
                        min_k = len(k)
    return getPath(sx, sy, min_k)


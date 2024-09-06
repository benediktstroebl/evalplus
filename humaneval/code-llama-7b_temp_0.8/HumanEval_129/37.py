
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
    n, m = len(grid), len(grid[0])
    d = [[float('inf') for i in range(m)] for j in range(n)]
    d[0][0] = grid[0][0]
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            x1, y1 = x+dx, y+dy
            if 0 <= x1 < n and 0 <= y1 < m:
                d[x1][y1] = min(d[x1][y1], d[x][y] + grid[x1][y1])
                q.append((x1, y1))
    return [d[n-1][m-1]] + [d[i][j] for i in range(n) for j in range(m) if d[i][j] != float('inf')]



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
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return []
    h, w = len(grid), len(grid[0])
    if h * w < k:
        return []

    def gen_coord(r, c):
        return r * w + c

    dp = {}
    visited = set()

    def bfs(r, c, k):
        if (r, c) in visited or (r, c) in dp:
            return
        visited.add((r, c))
        if k == 1:
            dp[(r, c)] = [grid[r][c]]
            return

        candidates = []
        for r_ in range(max(0, r - 1), min(h, r + 2)):
            for c_ in range(max(0, c - 1), min(w, c + 2)):
                if (r_, c_) != (r, c):
                    candidates.append((r_, c_))

        for r_, c_ in candidates:
            bfs(r_, c_, k - 1)
            if (r_, c_) in dp:
                dp[(r, c)] = [grid[r][c]] + dp[(r_, c_)]

    for r in range(h):
        for c in range(w):
            bfs(r, c, k)
            if (r, c) in dp:
                return dp[(r, c)]

    return []


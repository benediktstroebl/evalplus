
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
    m = len(grid)
    n = len(grid[0])

    if m == 0 or n == 0 or k == 0:
        return []

    if k == 1:
        return [i for i in range(1, n * m + 1)]

    graph = get_graph(grid, m, n)
    if k == n * m:
        return [i for i in range(1, n * m + 1)]

    cands = {(i, j): set() for i in xrange(m) for j in xrange(n) if grid[i][j] == 0}
    if len(cands) == k and k == 1:
        return [graph[cands.keys()[0]][0]]

    for i in xrange(1, n + 1):
        for j in xrange(1, m + 1):
            if grid[j - 1][i - 1] == 0:
                cands[(j, i)].add(0)
                continue

            cands[(j, i)].add(grid[j - 1][i - 1])

    for lst in cands.values():
        lst.add(0)

    def check(cand):
        for i in cand:
            cands[i].remove(0)
            if len(cands[i]) == 0:
                del cands[i]

    cands[cands.keys()[0]].remove(0)

    while k > 0:
        if not cands:
            return []

        cand = cands.keys()[0]
        check(cands[cand])
        k -= 1

    if k == 0:
        return [grid[cand[0] - 1][cand[1] - 1]]

    def check_right(cand):
        if cand[0] + 1 < m:
            cands[(cand[0] + 1, cand[1])].add(cand[0] * n + cand[1] - 1)
            cands[(cand[0] + 1, cand[1])].remove(cand[0] * n + cand[1] - 1)

    def check_left(cand):
        if
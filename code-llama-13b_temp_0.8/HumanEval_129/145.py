
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
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    # 0.12
    # 0.09
    # 0.06
    # 0.05
    rn, cn = len(grid), len(grid[0])
    if k >= rn+cn-1:
        return [1]
    m = [[-1 for _ in range(cn+1)] for _ in range(rn+1)]
    m[0][0] = 0
    for i in range(1, rn+1):
        for j in range(1, cn+1):
            if m[i-1][j] != -1:
                m[i][j] = m[i-1][j] + grid[i-1][j-1]
            if m[i][j-1] != -1:
                m[i][j] = min(m[i][j], m[i][j-1] + grid[i-1][j-1])
    path = []
    for _ in range(k):
        if m[-2][-2] != -1:
            path.append(grid[-2][-2])
            m[-2][-2] = -1
        else:
            path.append(grid[-1][-1])
            m[-1][-1] = -1
        if m[-2][-2] != -1 and m[-1][-1] != -1:
            m[-1][-1] = min(m[-1][-1], m[-2][-2])
        if m[-2][-2] != -1 and m[-1][-2] != -1:
            m[-1][-2] = min(m[-1][-2], m[-2][-2])
        if m[-1][-2] != -1 and m[-2][-1] != -1:
            m[-2][-1] = min(m[-2][-1], m[-1][-2])
    return path


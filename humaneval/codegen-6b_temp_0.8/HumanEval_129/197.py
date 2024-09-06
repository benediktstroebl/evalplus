
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
    if not grid or not grid[0] or k == 0:
        return []

    rows, cols = len(grid), len(grid[0])
    m = min(rows, cols)

    if k >= 2 * m:
        return [grid[i][j] for i in range(rows) for j in range(cols)]

    dist = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dist[i][j] = float('inf') if i == j else grid[i][j]

    for w in range(2, m + 1):
        for i in range(rows - w + 1):
            j = i + w - 1
            for m_i, m_j in ((i, j), (j, i)):
                for to_i, to_j in ((m_i + 1, m_j), (m_i, m_j + 1)):
                    if dist[m_i][m_j] + grid[to_i][to_j] < dist[to_i][to_j]:
                        dist[to_i][to_j] = dist[m_i][m_j] + grid[to_i][to_j]

    for i in range(rows - k + 1):
        for j in range(cols - k + 1):
            if dist[i][j] < float('inf'):
                return [grid[i][j]] + minPath(grid, k - 1)
    return []


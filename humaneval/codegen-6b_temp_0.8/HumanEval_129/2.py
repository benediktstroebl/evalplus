
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
    from collections import deque
    if not grid or not grid[0]:
        return []
    n = len(grid)
    m = len(grid[0])
    if m == 1 and n == 1:
        return grid[0]
    if k == 0:
        return []
    if k > n * m:
        return minPath(grid, n * m - 1)
    if k == n * m:
        return grid[-1]
    INF = int(1e9)
    minVisited = [[INF] * m for _ in range(n)]
    minVisited[0][0] = grid[0][0]
    queue = deque()
    queue.append((0, 0))
    while queue:
        pos = queue.popleft()
        for i, j in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
            if 0 <= i < n and 0 <= j < m:
                if i == n - 1 and j == m - 1:
                    continue
                if minVisited[i][j] == INF:
                    minVisited[i][j] = grid[i][j]
                    queue.append((i, j))
                elif minVisited[i][j] != INF and minVisited[i][j] > grid[i][j]:
                    minVisited[i][j] = grid[i][j]
                    queue.append((i, j))
    ret = minVisited[n - 1][m - 1]
    if ret == INF:
        return []
    res = [ret]
    queue = deque()
    queue.append((n - 1, m - 1))
    while queue:
        pos = queue.popleft()
        for i, j in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
            if 0 <= i < n and 0 <= j
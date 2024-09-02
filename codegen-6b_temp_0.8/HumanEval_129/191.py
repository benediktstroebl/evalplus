
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
    rows, cols = len(grid), len(grid[0])
    if rows == 1 or cols == 1:
        return grid[0]

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    dist = [[0 for _ in range(cols)] for _ in range(rows)]
    q = deque()
    means = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            pathLength = min(dist[row][col],k)
            if pathLength > 0:
                means[row][col] = grid[row][col]
            if not visited[row][col]:
                visited[row][col] = True
                dist[row][col] += 1
                if pathLength > 0:
                    q.append((row, col, 0, None))
                else:
                    q.append((row, col, pathLength, None))

    def isLegal(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def getNeighbors(row, col):
        neighbors = []
        if isLegal(row-1, col):
            neighbors.append((row-1, col, dist[row-1][col], means[row-1][col]))
        if isLegal(row+1, col):
            neighbors.append((row+1, col, dist[row+1][col], means[row+1][col]))
        if isLegal(row, col-1):
            neighbors.append((row, col-1, dist[row][col-1], means[row][col-1]))
        if isLegal(row, col+1):
            neighbors.append((row, col+1, dist[row][col+1], means[row][col+1]))
        return neighbors

    while q:
        row, col, pathLen, means_ = q.popleft()
        neighbors = getNeighbors(row
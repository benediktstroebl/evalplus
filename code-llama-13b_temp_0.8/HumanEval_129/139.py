
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
    M = len(grid)
    N = len(grid[0])
    # 2D grid has at most 2 neighbors
    # 2D grid with wrap-around has at most 3 neighbors
    # Create a matrix that stores neighboring cells for each cell
    neighbors = [[[] for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if i != 0:
                neighbors[i][j].append((i - 1, j))
            if i != M - 1:
                neighbors[i][j].append((i + 1, j))
            if j != 0:
                neighbors[i][j].append((i, j - 1))
            if j != N - 1:
                neighbors[i][j].append((i, j + 1))
    # Store the number of steps we took to reach a cell
    dist = [[float("inf") for _ in range(N)] for _ in range(M)]
    # Number of cells visited so far
    cnt = [[0 for _ in range(N)] for _ in range(M)]
    q = deque([(0, 0, 0, [])])
    while q:
        (x, y, steps, path) = q.popleft()
        if steps == k and cnt[x][y] < M * N:
            return path + [grid[x][y]]
        for (a, b) in neighbors[x][y]:
            if dist[a][b] > steps + 1:
                dist[a][b] = steps + 1
                cnt[a][b] = cnt[x][y] + 1
                q.append((a, b, steps + 1, path + [grid[x][y]]))








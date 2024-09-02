
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
    def isValid(x, y):
        return 0 <= x < m and 0 <= y < m

    def neighbor(x, y):
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx = x + dx
            ny = y + dy
            if isValid(nx, ny):
                yield nx, ny

    m = len(grid)
    # build the adjacency list
    adj_list = {(x, y): [] for x in range(m) for y in range(m)}
    for i in range(m):
        for j in range(m):
            if j + 1 < m:
                adj_list[(i, j)].append((i, j + 1))
            if i + 1 < m:
                adj_list[(i, j)].append((i + 1, j))
    # build the adjacency matrix
    adj_matrix = {(i, j): 0 for i in range(m) for j in range(m)}
    for i in range(m):
        for j in range(m):
            for x, y in neighbor(i, j):
                adj_matrix[(i, j)] |= 1 << (x * m + y)
    # build the graph
    g = {i: set() for i in range(m * m)}
    for i in range(m * m):
        for j in range(m * m):
            if adj_matrix[(i % m, i // m)] & adj_matrix[(j % m, j // m)]:
                g[i].add(j)
    # build the distance array
    dist = [float('inf')] * (m * m)
    visited = [False] * (m * m)
    def bfs(i):
        d = 0
        q = deque([i])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if visited[cur]:
                    continue
                visited[cur] = True
                if d == k:
                    return cur

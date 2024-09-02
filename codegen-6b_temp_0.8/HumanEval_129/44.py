
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
    N = len(grid)  # number of rows and columns

    if k > (N * N):
        return list(range(1, N * N + 1))

    if k == 0:
        return []

    if k == (N * N):
        return grid[-1][-1]

    if N == 1:
        return grid[0][0]

    # build graph
    graph = defaultdict(list)  # directed graph
    for r in range(N):
        for c in range(N):
            if r > 0:
                graph[(r, c)].append((r - 1, c))
            if c > 0:
                graph[(r, c)].append((r, c - 1))

    # Dijkstra's algorithm
    q = [(grid[0][0], 0, 0)]  # (value, r, c)
    heapq.heapify(q)
    visited = [[False for _ in range(N)] for _ in range(N)]  # visited[r][c] == True means that the path from 0
    #  to (r, c) is visited
    visited[0][0] = True  # visited[0][0] == True means that the path from 0 to 0 is visited
    while len(q) > 0:
        v, r, c = heapq.heappop(q)
        # v == grid[r][c]
        # r == r
        # c == c
        if r == N - 1 and c == N - 1:  # (r, c) is the goal
            return v
        for rr, cc in graph[(r, c)]:
            if not visited[rr][cc]:
                # we visited (rr, cc) before
                # so the current path from (r, c) to (rr, cc) is longer
                # so we need to replace the current cost with the new cost
                heapq.heappush(q, (v + grid[rr][cc], rr, cc))
                visited[rr][cc] = True



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
    # construct the graph
    n = len(grid)

    # cache the (u,v) - > min_path
    # edges[u][v] = min_path from u to v
    edges = [[None for j in range(n)] for i in range(n)]

    # construct the graph
    for u in range(n):
        for v in range(n):
            edges[u][v] = grid[u][v]

    # calculate the min path to all the nodes
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i > 0 and edges[i][j] > edges[i - 1][j] + grid[i][j]:
                edges[i][j] = edges[i - 1][j] + grid[i][j]

            if j > 0 and edges[i][j] > edges[i][j - 1] + grid[i][j]:
                edges[i][j] = edges[i][j - 1] + grid[i][j]

    # find the min path
    min_path_to_end = edges[-1][-1]
    k = min(k, min_path_to_end)

    # get the path from the end
    path = []
    u, v = n - 1, n - 1
    while k > 0:
        min_path = min(edges[u][v - 1], edges[u - 1][v])
        if min_path == edges[u - 1][v]:
            u -= 1
        else:
            v -= 1
        path.append(grid[u][v])
        k -= 1

    return path



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

    # # DFS Recursion
    # # TC: O(2^N)
    # # SC: O(N)
    # n = len(grid)

    # def dfs(i, j, length):
    #     if length == k:
    #         nonlocal res
    #         res = sorted(grid[i][j])
    #         return

    #     if i < 0 or i >= n or j < 0 or j >= n:
    #         return

    #     # do not use
    #     grid[i][j] = -1
    #     dfs(i - 1, j, length + 1)
    #     dfs(i + 1, j, length + 1)
    #     dfs(i, j - 1, length + 1)
    #     dfs(i, j + 1, length + 1)
    #     # use
    #     grid[i][j] = 0

    # res = []
    # for i in range(n):
    #     for j in range(n):
    #         dfs(i, j, 0)
    # return res

    # BFS
    # TC: O(N * K * 4^K)
    # SC: O(N)
    n = len(grid)
    visited = set()
    min_dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    # init
    for i in range(n):
        min_dist[i][0] = grid[i][0]
        visited.add((i, 0))

    # BFS
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if min_dist[i][k - 1] + grid[i][j] < min_dist[j][k]:
                    min_dist[j][k] = min_dist[i][k - 1] + grid[i][j]
                    visited.add((j, k))

    path = [0] * k
    i, j = 0, n - 1
    for k in range(k - 1, -1, -1):
        if min_dist[i][j] - grid[i][j] == min_dist[i][k - 1]:
            path[

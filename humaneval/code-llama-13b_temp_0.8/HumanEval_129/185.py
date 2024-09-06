
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
    visited = [[0] * N for _ in range(M)]
    cur = grid[0][0]
    visited[0][0] = 1
    queue = [(cur, 0, 0)]
    while queue:
        cur, i, j = queue.pop(0)
        if visited[i][j] != cur:
            visited[i][j] = cur
            if i + 1 < M and not visited[i + 1][j]:
                queue.append((visited[i][j], i + 1, j))
            if j + 1 < N and not visited[i][j + 1]:
                queue.append((visited[i][j], i, j + 1))
            if i - 1 >= 0 and not visited[i - 1][j]:
                queue.append((visited[i][j], i - 1, j))
            if j - 1 >= 0 and not visited[i][j - 1]:
                queue.append((visited[i][j], i, j - 1))
        if visited[i][j] == k:
            return visited[i][j]
        for val in queue:
            if val[0] != visited[i][j]:
                visited[i][j] = min(visited[i][j], val[0])
        if visited[M - 1][N - 1] >= k:
            return visited[M - 1][N - 1]

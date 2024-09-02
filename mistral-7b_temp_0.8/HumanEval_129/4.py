
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
    n = len(grid)
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == k:
                res = [i, j]
                break

    # if res is not found, then k is not in the grid, hence the answer is [-1]
    if len(res) == 0:
        return [-1]

    # try all possible paths with length k, find the shortest one, and record its value on each cell
    def dfs(path, k, start_i, start_j, visited, path_val, prev_val):
        if k == 0:
            if path not in res:
                res.append(path)
            return
        if k < 0:
            return
        for i in range(start_i-1, start_i+2):
            for j in range(start_j-1, start_j+2):
                if i >= 0 and i < n and j >= 0 and j < n and (i,j) not

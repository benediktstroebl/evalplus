
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
    # O(N^4) time, O(N^3) space
    grid_max = max(max(grid), k)
    def search(grid, k, i, j):
        if k == 0:
            return 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 10**10
        if grid[i][j] > k:
            return 10**10
        if grid[i][j] == k:
            return 0
        ret = min(search(grid, k, i+1, j), search(grid, k, i-1, j), search(grid, k, i, j+1), search(grid, k, i, j-1))
        if ret == 10**10:
            return 10**10
        else:
            return ret + 1
    grid_copy = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):

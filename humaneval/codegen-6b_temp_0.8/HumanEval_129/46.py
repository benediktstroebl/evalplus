
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
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0 or k == 0:
        return []

    visited = [[0] * n for _ in range(m)]
    memo = {}

    def dfs(row, col, remaining):
        if remaining <= 0:
            return float('inf')
        if row == m - 1 and col == n - 1:
            return 0

        if (row, col, remaining) in memo:
            return memo[(row, col, remaining)]

        prev, next_min = float('inf'), float('inf')

        if row < m - 1 and visited[row + 1][col] == 0:
            next_min = dfs(row + 1, col, remaining - 1) + grid[row + 1][col]
        if col < n - 1 and visited[row][col + 1] == 0:
            prev = dfs(row, col + 1, remaining - 1) + grid[row][col + 1]

        memo[(row, col, remaining)] = min(prev, next_min)
        return memo[(row, col, remaining)]

    return dfs(0, 0, k)


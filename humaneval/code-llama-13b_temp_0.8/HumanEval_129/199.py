
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
    """
    # idea: explore all the paths (use depth first search)
    #       and choose the one that ends at the cell with the required value
    def dfs(row, col, val):
        if not grid[row][col] == val:
            return False
        if row == N - 1 and col == N - 1:
            return True

        res = False
        # go down
        if row + 1 < N and grid[row + 1][col] < val:
            res = res or dfs(row + 1, col, val)
        # go right
        if col + 1 < N and grid[row][col + 1] < val:
            res = res or dfs(row, col + 1, val)
        # go up
        if row - 1 >= 0 and grid[row - 1][col] < val:
            res = res or dfs(row - 1, col, val)
        # go left
        if col - 1 >= 0 and grid[row][col - 1] < val:
            res = res or dfs(row, col - 1, val)

        return res

    N = len(grid)
    return [
        i
        for i in range(1, N * N + 1)
        if dfs(0, 0, i) and dfs(N - 1, N - 1, i + k - 1)
    ]
    """
    # idea: dynamic programming
    # we can go from any cell to any of its neighbor, so grid can be seen as a graph
    # with cell as nodes and edges between neighboring cells
    # we need to get from cell (0, 0) to (N - 1, N - 1) with length exactly k
    # we can treat each edge as a variable and we need to find all the paths
    # that pass through every edge at least once and we are only allowed to visit
    # a cell at most once
    # number of paths: dp[i][j][c] is the number of paths that start from cell (i, j)
    # and have length k (k - c) and they

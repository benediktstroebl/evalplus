
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

    N = len(grid)
    # Let's create an empty table for memoization
    table = [[None for i in range(N)] for i in range(N)]

    def helper(i, j, k, grid):
        # Base case
        if k == 0:
            return []
        # Check if the answer is already in the table
        if table[i][j] is not None:
            return table[i][j]
        # Check if we've reached the end of the grid
        if i == N-1 and j == N-1:
            return grid[i][j]

        # If we're at the end of the row, go down
        if j == N-1:
            answer = [grid[i][j]] + helper(i+1, j, k-1, grid)
        # If we're at the end of the column, go right
        elif i == N-1:
            answer = [grid[i][j]] + helper(i, j+1, k-1, grid)
        # Otherwise, go right or down depending on the optimal answer
        else:
            right = grid[i][j] + helper(i, j+1, k-1, grid)
            down = grid[i][j] + helper(i+1, j, k-1, grid)
            answer = [grid[i][j]] + min(right, down, key=len)

        # Insert the answer in the table
        table[i][j] = answer

        return answer

    return helper(0, 0, k, grid)

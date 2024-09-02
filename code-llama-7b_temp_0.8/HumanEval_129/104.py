
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
    assert N >= 2
    # Create a new grid with the same dimension
    newGrid = [[0] * N for i in range(N)]

    # Calculate the distance from each cell to each corner
    for i in range(N):
        for j in range(N):
            newGrid[i][j] = min(grid[i][0] + j, grid[0][j] + i)
            newGrid[i][j] += min(grid[N - 1 - i][j] + N - 1 - i,
                                 grid[i][N - 1 - j] + N - 1 - j)

    # Create the dp table
    dp = [[None for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = newGrid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j] + grid[i][j],
                               dp[i][j - 1] + grid[i][j])

    cur = dp[N - 1][N - 1]
    res = []
    for i in range(k):
        if i % 2 == 0:
            res.append(grid[N - 1][N - 1])
            cur -= grid[N - 1][N - 1]
            if cur < 0:
                raise Exception('Cur should not be smaller than 0')
        else:
            x, y = N - 1, N - 1
            while cur <= newGrid[x][y]:
                if x == 0:
                    y -= 1
                elif y == 0:

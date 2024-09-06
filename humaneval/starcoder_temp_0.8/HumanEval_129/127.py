
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
    k = min(k, n * n)

    dp = [[[math.inf for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]

    # Initialize the value at the first cell
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j][1] = grid[0][0]

    # Solve for the rest of the cells
    for i in range(n):
        for j in range(n):
            if i == 0 and j!= 0:
                for z in range(1, k + 1):
                    if j - 1 < 0 or z < j:
                        continue
                    dp[i][j][z] = min(dp[i][j][z], dp[i][j - 1][z - 1] + grid[i][j])
            elif i!= 0 and j == 0:
                for z in range(1, k + 1):
                    if i - 1 < 0 or z < i:
                        continue
                    dp[i][j][z] = min(dp[i][j][z], dp[i - 1][j][z - 1] + grid[i][j])
            else:
                for z in range(1, k + 1):
                    if i - 1 < 0 or z < i or j - 1 < 0 or z < j:
                        continue
                    dp[i][j][z] = min(
                        dp[i][j][z], dp[i - 1][j][z - 1] + grid[i][j], dp[i][j - 1][z - 1] + grid[i][j])

    res = []
    x, y = n - 1, n - 1
    z = k

    while z > 0:
        res.append(grid[x][y])

        if z == k or z - 1 == 0:
            break

        # Check if the neighboring cell is more preferred
        if x > 0 and dp[x - 1][y][z - 1] + grid[x - 1][y] < dp[x][y - 1][z - 1

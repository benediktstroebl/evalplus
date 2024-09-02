
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
    def compare(lst_a, lst_b):
        for i in range(k):
            if lst_a[i] < lst_b[i]:
                return True
            if lst_a[i] > lst_b[i]:
                return False
        return False

    if not grid or not grid[0] or k < 1:
        return []

    n = len(grid)
    m = len(grid[0])

    if k > (n * m):
        return []

    visited = [[[False for _ in range(k)] for _ in range(m)] for _ in range(n)]
    min_path = 0

    for i in range(n):
        for j in range(m):
            # if row = 0, col = 0 is the top left corner
            if i == 0 and j == 0:
                if grid[i][j] > 0:
                    min_path += grid[i][j]
            else:
                if grid[i][j] > 0:
                    # down
                    if grid[i][j] < grid[i - 1][j] and not visited[i][j][min_path]:
                        min_path += grid[i][j]
                        visited[i][j][min_path] = True
                    # left
                    if grid[i][j] < grid[i][j - 1] and not visited[i][j][min_path]:
                        min_path += grid[i][j]
                        visited[i][j][min_path] = True
                    # check current cell
                    if compare(grid[i][j], grid[i - 1][j]) and not visited[i][j][min_path]:
                        min_path += grid[i][j]
                        visited[i][j][min_path] = True

    res = []
    while min_path > 0:
        res += grid[n - 1][m - 1]
        min_path -= grid[n - 1][m - 1]
        n -= 1
        m -= 1
        if n == 0:
            break
        if min_path >= grid[n][m]:
            break

    
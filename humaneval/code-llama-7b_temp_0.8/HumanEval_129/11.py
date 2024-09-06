
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
    if len(grid) < 2 or len(grid[0]) < 2: return []
    N, M = len(grid), len(grid[0])
    if k > N*M: return []

    def build_min_path_d_table(grid):
        N, M = len(grid), len(grid[0])
        d = [[[float('inf')] for _ in range(M)] for _ in range(N)]
        d[0][0] = grid[0][0]
        for i in range(N):
            for j in range(M):
                if i == 0 and j != 0:
                    d[i][j] = min(d[i][j - 1], d[i][j]) + grid[i][j]
                elif j == 0 and i != 0:
                    d[i][j] = min(d[i - 1][j], d[i][j]) + grid[i][j]
                elif i != 0 and j != 0:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i][j]) + grid[i][j]
        return d

    def find_path(d, k):
        N, M = len(grid), len(grid[0])
        path = []
        i, j = N - 1, M - 1
        while k > 0:
            k -= 1
            path.append(d[i][j])
            if i == 0 and j == 0: break
            if i == 0:
                j -= 1
                continue
            if j == 0:
                i -= 1
                continue
            d_left = d[i][j - 1]
            d_top = d[i - 1][j]
            d_top_left = d[i - 1][j - 1]
            if d_left < min(d_top, d_top_left):
                j -= 1
            elif d_top < min(d_left, d_top_left):
                i

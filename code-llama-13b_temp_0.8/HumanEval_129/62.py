
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
    def min_path(k):
        # result = []
        # we have two DP table: DP and DP2.
        # DP[i][j] indicates the min path length from (0,0) to (i,j)
        # DP2[i][j] indicates the kth smallest path from (0,0) to (i,j)
        DP = [[0] * (c + 1) for _ in range(r + 1)]
        DP2 = [[[] for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                # first, find the min path length
                if i == 0 and j == 0:
                    DP[i + 1][j + 1] = grid[i][j]
                else:
                    # if it is not the first row or col, find the min path from
                    # (i - 1, j) and (i, j - 1)
                    min_val = min(DP[i][j + 1], DP[i + 1][j])
                    DP[i + 1][j + 1] = min_val + grid[i][j]

                # now add the val to its kth smallest path
                if i == 0 and j == 0:
                    DP2[i + 1][j + 1] = [grid[i][j]]
                else:
                    if DP[i + 1][j + 1] == DP[i][j + 1]:
                        DP2[i + 1][j + 1].extend(DP2[i][j + 1])
                    if DP[i + 1][j + 1] == DP[i + 1][j]:
                        DP2[i + 1][j + 1].extend(DP2[i + 1][j])

        # get the smallest kth path
        return DP2[r][c][k - 1]

    # check corner case
    if k <= 

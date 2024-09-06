
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
    M = len(grid[0])
    # we can get n^2 numbers, so we need to store them
    # it's very hard to extend the size of this array
    # so we need to use two pointers to compare worse case.
    # Note: the space is O(N^2) in worst case
    # but we know that n^2 <= 10^4, so it's OK to use array instead of dict
    p2 = [0] * N * N
    p1 = [0] * N * N
    max_val = -1
    max_idx = -1
    for i in range(N):
        for j in range(M):
            max_idx = i * M + j
            max_val = max(max_val, grid[i][j])

            if i - 1 >= 0:
                p2[max_idx] = max(p2[max_idx], p2[max_idx - M] + grid[i - 1][j])
            if j - 1 >= 0:
                p2[max_idx] = max(p2[max_idx], p2[max_idx - 1] + grid[i][j - 1])
            if i - 1 >= 0 and j - 1 >= 0:
                p2[max_idx] = max(p2[max_idx], p2[max_idx - M - 1] + grid[i - 1][j - 1])

            if i + 1 < N:
                p1[max_idx] = max(p1[max_idx], p1[max_idx - 1] + grid[i + 1][j])
            if j + 1 < M:
                p1[max_idx] = max(p1[max_idx], p1[max_idx - M] + grid[i][j + 1])
            if i + 1 < N and j + 1 < M:
                p1[max_idx] = max(p1[max_idx], p1[max_idx - M - 1] + grid[i + 1][j + 1])

    lst
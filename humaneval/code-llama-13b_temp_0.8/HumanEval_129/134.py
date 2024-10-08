
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
    # Get a list of the smallest sum path, a list of the smallest sum path.
    # At each step, look at the neighbors to the current cell, if the value is
    # smaller than the current best path, then replace it in the list.
    N = len(grid)
    bestSum = [[0 for _ in range(N)] for _ in range(N)]
    bestPath = [[[] for _ in range(N)] for _ in range(N)]
    bestSum[0][0] = grid[0][0]
    bestPath[0][0] = [grid[0][0]]
    for i in range(N):
        for j in range(N):
            # If we are at the first row or column, then bestSum and bestPath are
            # the same as the previous row or column.
            if i == 0:
                bestSum[i][j] = bestSum[i][j - 1] + grid[i][j]
                bestPath[i][j] = bestPath[i][j - 1] + [grid[i][j]]
            elif j == 0:
                bestSum[i][j] = bestSum[i - 1][j] + grid[i][j]
                bestPath[i][j] = bestPath[i - 1][j] + [grid[i][j]]
            else:
                bestSum[i][j] = min(bestSum[i - 1][j], bestSum[i][j - 1]) + grid[i][j]
                if bestSum[i - 1][j] < bestSum[i][j - 1]:
                    bestPath[i][j] = bestPath[i - 1][j] + [grid[i][j]]
                else:
                    bestPath[i][j] = bestPath[i][j - 1] + [grid[i][j]]
    # Now, we just need to find the kth smallest path.
    res = []
    # We are going to find the kth element in a list of the smallest paths
    # (bestPath).
    # The number of elements in the list is equal to N^2 - k + 


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
    # This is a tricky question, very difficult to understand, especially
    # the two constraints, no k steps off the grid and k can be bigger than n.
    # After several test cases, I found the answer is not unique.
    # The following code is based on the answer by creamofcof:
    # https://leetcode.com/problems/minimum-path-with-k-steps/discuss/137948/JavaPython-4-2-lines-2-minor-optimization-and-3-tricks
    # The tricks are:
    # 1. The answer is unique.
    # 2. The starting point doesn't matter.
    # 3. Use the relative position instead of the coordinates to avoid "no k steps off the grid".
    # 4. Keep a min list with the previous lowest value instead of keeping a min matrix.
    # 5. The order of the answer should be from the starting point to the ending point.
    # 6. Note that when an int in a list is smaller than any of the other ints in the list,
    #    the list is sorted.

    n, m = len(grid), len(grid[0])
    min_path = [0] * n  # the minimum path of length k-1
    min_path[0] = grid[0][0]
    for i in range(1, n):
        min_path[i] = min(grid[0][i], min_path[i - 1])
    for i in range(1, m):
        min_path[0] = min(min_path[0], grid[i][0])
        for j in range(1, n):
            min_path[j] = min(grid[i][j] + min_path[j - 1], min_path[j])
    return [min_path[n - 1]] + min_path

    # Solution 1:
    # dp = [[float('inf')] * n for _ in range(n)]
    # dp[0][0] = grid[0][0]
    # for i in range(1, n):
    #     d

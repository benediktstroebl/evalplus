
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
    # Warm-up: minimum path in a 2D array
    # There is only one path of length k in a 2D array.
    # Return the minimum path in the 2D array.
    # The path's length is k.
    # A path A is considered less than a path B if A[0] < B[0] and for any 1 <= i < k, A[i] <= B[i].
    # For example, if k = 5:
    # [1, 3, 1, 4, 1] is less than [2, 1, 1, 3, 2] because A[0] = 1 < B[0] = 2,
    # and for 1 <= i < 5, A[i] <= B[i] (1 <= A[i] <= 1, 1 <= A[i] <= 1, 1 <= A[i] <= 3, and 1 <= A[i] <= 2).
    def minimumPath(grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        p = [grid[0][0]]
        i = 0
        j = 0
        while len(p) < k:
            if j + 1 < n and grid[i][j + 1] < grid[i][j]:
                j += 1
            else:
                i += 1
            p.append(grid[i][j])
        return p[:k]

    def min_path(grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # https://www.cnblogs.com/grandyang/p/7700122.html
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = 0
        for i

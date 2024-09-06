
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
    # O(n^2) time complexity, O(n^2) space complexity
    # works fine, but the time complexity is too high
    #
    # better to use DP, the time complexity of which is 
    # O(k*n^2)
    # 
    # still O(n^2) space complexity
    #
    # however, this is the second question from this week, the first question is
    # Leetcode 200: Number of Islands. It is a tricky question.
    # 
    # I am sure there is some tricks that I missed.
    # 
    # I will try to solve it again.
    #
    #
    # solutions by other people:
    # https://leetcode.com/problems/minimum-length-path-in-a-grid/discuss/68388/
    #
    #
    #
    #
    def path_length(i, j, k):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
            return float('inf')
        if k == 0:
            return 0
        if grid[i][j] == 0:
            return float('inf')

        return grid[i][j] + min(path_length(i-1, j, k-1),
                                path_length(i+1, j, k-1),
                                path_length(i, j-1, k-1),
                                path_length(i, j+1, k-1))

    min_path = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            min_path.append(path_length(i, j, k))

    min_path.sort()
    return min_path



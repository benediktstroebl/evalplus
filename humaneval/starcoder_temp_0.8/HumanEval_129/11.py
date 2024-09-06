
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

    def is_possible(x, y, k):
        """
        Check if a certain path is possible or not.
        It is possible if in the last step we reach a possible point, or if the 
        last step is a horizontal or a vertical step.
        """
        return (x == 0 and y == 0) or (x == 0 and y == k) or (y == 0 and x == k)

    def solve(i, j, k):
        """
        Dynamic programming algorithm.
        """
        if k == 1:
            return (0, 0)

        (k1, k2) = solve(i, j - 1, k - 1) if is_possible(i, j, k) else (INF, INF)
        (k3, k4) = solve(i - 1, j, k - 1) if is_possible(i, j, k) else (INF, INF)
        k = min(k1, k2, k3, k4)

        if k == k1:
            return (1 + k1, j)
        elif k == k2:
            return (1 + k2, j - 1)
        elif k == k3:
            return (1 + k3, j)
        elif k == k4:
            return (1 + k4, j)

    # Solve the problem and return the minimum path.
    return [grid[i][j] for i, j in solve(len(grid) - 1, len(grid[0]) - 1, k)]


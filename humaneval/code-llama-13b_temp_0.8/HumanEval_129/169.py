
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
    def min_path_helper(grid, i, j, k):
        # Return the minimum path that starts from the i-th row and j-th column
        # of grid and has length k
        if k == 0: return []

        if i == len(grid) or j == len(grid[i]):
            return None
        
        if k == 1:
            return [grid[i][j]]

        min_path = None
        # Try all neighbors
        for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]):
                tmp = min_path_helper(grid, x, y, k-1)
                if tmp is not None:
                    if min_path is None or tmp[:k-1] < min_path[:k-1]:
                        min_path = tmp
        
        if min_path is None:
            return None
        else:
            return [grid[i][j]] + min_path

    # Find the minimum path starting from the upper-left corner
    min_path = min_path_helper(grid, 0, 0, k)
    # Find the minimum path starting from the lower-left corner
    min_path2 = min_path_helper(grid, len(grid)-1, 0, k)
    # Find the minimum path starting from the upper-right corner
    min_path3 = min_path_helper(grid, 0, len(grid[0])-1, k)
    # Find the minimum path starting from the lower-right corner
    min_path4 = min_path_helper(grid, len(grid)-1, len(grid[0])-1, k)

    if min_path is None:
        return min_path2
    elif min_path2 is None:
        return min_path
    else:
        return min_path if min_path < min_path2 else min_path2

    if min_path3 is None:
        return min_

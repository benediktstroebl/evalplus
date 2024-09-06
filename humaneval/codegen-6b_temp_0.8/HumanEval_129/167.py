
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
    if not grid or not grid[0]:
        return None
    if k == 1:
        return sorted([num[0] for num in grid])
    
    rows, cols = len(grid), len(grid[0])
    
    # For each cell, we will store the minimum value from the cell above and 
    # the cell to the right.
    min_vals = [None] * (rows * cols)
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                # first cell (top left corner)
                min_vals[0] = grid[0][0]
            elif j == 0:
                # leftmost column
                min_vals[j] = min_vals[j - 1] + grid[i][j]
            else:
                min_vals[j] = min(min_vals[j - 1], min_vals[j]) + grid[i][j]

    # Now we want to find the min values that we have calculated
    min_vals = min_vals[-1]
    # start from the highest row and the last column
    while k > 0 and min_vals:
        min_vals = min_vals[k - 1]
        k -= 1
    return min_vals



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
    if k == 1:
        return [min(grid[0])]
    elif k == 2:
        return [min(grid[0] + grid[1])]
    elif k == 3:
        return [min(grid[0] + grid[1] + grid[2])]

    # 1. we are going to use bottom-up approach
    # 2. we are going to store the pathes in the matrix
    #    where the first row and column contain the paths to i-th
    #    and j-th cell of the grid
    # 3. we are going to store the pathes in reverse order
    #    i.e. for k = 3 it will be [[1, 2, 1], [2, 1], [1]]
    # 4. to get the final pathes we will reverse the array
    # 5. we are going to use lexicographically comparison
    #    for paths, i.e. the algorithm will return the shortest
    #    pathes first

    n = len(grid)
    pathes = [[None] * n for _ in range(k)]
    pathes[0][0] = grid[0][0]
    pathes[0][1:] = grid[0][1:]
    pathes[1][:2] = grid[0][:2]
    pathes[1][2] = grid[0][2]

    for step in range(2, k):
        # we are going to fill the cells one row at a time
        # the first row is already filled, so we start from the second one
        row = step + 1
        for col in range(row, n):
            if row == col:
                # the case when we are on the diagonal
                # we have only one path
                pathes[step][col] = grid[row - 1][col]
            else:
                # in other cases we have two paths
                # first is from the upper cell
                # second is from the left cell
                pathes[step][col] = min(pathes[step - 1][col - 1], pathes[step - 1][col])
                path

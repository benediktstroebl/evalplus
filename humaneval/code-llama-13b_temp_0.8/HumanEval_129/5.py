
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

    def findPath(grid, k):
        if len(grid) == 0:
            return False
        if k == 1:
            return [grid[0][0]]

        if k > len(grid)*len(grid[0]):
            return False

        for row in grid:
            if len(row) != len(grid[0]):
                return False

        minPath = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # find a starting point
                if grid[i][j] == 1:
                    # find path
                    path = findPathHelper(grid, i, j, k-1)
                    if path:
                        minPath.append(path)

        if len(minPath) > 0:
            return minPath[0]
        else:
            return []

    def findPathHelper(grid, i, j, k):
        # base cases
        # current grid[i][j] > k
        if grid[i][j] > k:
            return False
        # current grid[i][j] == k
        if grid[i][j] == k:
            return [k]

        # check if the current grid[i][j] < k
        # find the next grid cell
        if i > 0:
            cellUp = findPathHelper(grid, i-1, j, k-grid[i][j])
            if cellUp:
                cellUp.append(grid[i][j])
                return cellUp
        if i < len(grid)-1:
            cellDown = findPathHelper(grid, i+1, j, k-grid[i][j])
            if cellDown:
                cellDown.append(grid[i][j])
                return cellDown
        if j > 0:
            cellLeft = findPathHelper(grid, i, j-1, k-grid[i][j])
            if cellLeft:
                cellLeft.append(grid[i][j])
                return cellLeft
        if j < len(grid[0])-1:
            cellRight = findPath


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
    # check rows and columns
    if len(grid) < 2:
        return []
    if len(grid) == 2:
        return [grid[0][0]]

    # create an empty list to store the result
    result = []

    # iterate through all cells
    for i in range(len(grid[0])):
        # check the value of the cell
        if grid[i][0] == 0:
            # we cannot find a path with length k
            return []

        # check the cells that can be reached by moving in the direction of the arrow
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for j in range(len(grid)):
            for c in dx:
                if j == i:
                    continue
                path = minPath(grid, j, c)
                for p in path:
                    result.append(grid[i][j])
                    grid[i][j] = grid[p[0]][j]
                    grid[p[0]][j] = grid[i][j]
                    grid[i][j] = grid[i][j]

    # the path is finished, restore the grid
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            grid[i][j] = grid[i][j]

    # reverse the order of the result, because the order doesn't matter
    result = sorted(result, reverse=True)
    return result
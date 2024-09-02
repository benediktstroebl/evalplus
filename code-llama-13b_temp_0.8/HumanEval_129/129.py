
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
    # Create a new matrix, newGrid, which is the same size as grid.
    newGrid = []
    for i in range(len(grid)):
        newGrid.append([])
        for j in range(len(grid[0])):
            newGrid[i].append(0)

    # Iterate through grid, and set each cell to the value in the cell, 
    # plus the max of the two neighboring cells.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i-1 >= 0 and j-1 >= 0:
                newGrid[i][j] += max(grid[i-1][j-1], grid[i][j-1])
            elif i-1 >= 0:
                newGrid[i][j] += grid[i-1][j]
            elif j-1 >= 0:
                newGrid[i][j] += grid[i][j-1]

    # Fill in the next row, in reverse.
    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid[0])-1, -1, -1):
            if i+1 < len(grid) and j-1 >= 0:
                newGrid[i][j] += max(newGrid[i+1][j], newGrid[i][j-1])
            elif i+1 < len(grid):
                newGrid[i][j] += newGrid[i+1][j]
            elif j-1 >= 0:
                newGrid[i][j] += newGrid[i][j-1]

    # Starting at (0, 0), take k steps to the right.
    # Starting at (0, len(grid[0])-1), take k steps to the left.
    # Take the maximum of these two paths.
    # Return that path.

    def getPath(grid, pos, steps):
        if steps == 0:
            return [grid[pos[0]][pos[1]]]

        if pos[1] + steps >= len(grid[0]):
            return

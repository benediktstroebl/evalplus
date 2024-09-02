
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
    # check if grid is valid
    if len(grid) < 2:
        return []
    # check if grid is completely filled
    if grid == [[0 for _ in range(len(grid[0]))]: [0 for _ in range(len(grid))]]:
        return []
    # check if grid is completely empty
    if all(grid[i] == [0 for _ in range(len(grid))] for i in range(len(grid))):
        return []
    # put grid in 1-based form
    grid = [row + (row[0] - 1) * len(grid[0]) for row in grid]
    # 2-d list to store minimum path
    path = [None] * len(grid)
    # 2-d list to store visited cells
    visited = [None] * len(grid)
    # helper function to check if a path is valid
    def isValidPath(path):
        for i in range(len(path) - 1):
            # if path goes left
            if path[i] < path[i + 1]:
                return False
            # if path goes right
            if path[i] > path[i + 1]:
                return False
            # if path goes down
            if path[i + 1] < path[i]:
                return False
        return True
    # initialize path with [None]
    path[0] = (0, 0)
    # DFS
    visited[0] = True
    while len(path) < k:
        # find the next unvisited cell
        cell = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != 0:
                    cell = (i, j)
                    break
        if cell is None:
            return []
        # update path
        path[len(path) - 1] = (cell[0] - 1, cell[1])
        # mark the cell as visited
        visited[cell[0] - 1][cell[1]] = True
        # recursively check if the

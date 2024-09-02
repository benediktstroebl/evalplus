
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
    rows, cols = grid.shape

    # create a 2D empty list to store the path
    path = [[0 for j in range(cols)] for i in range(rows)]

    # mark the cells that have been visited
    visited = [[False for j in range(cols)] for i in range(rows)]

    # use a queue to store the cells that have to be visited next
    queue = [(0, 0)]

    # add the cell (0, 0) to the queue
    while queue:
        # get the next cell to visit
        cell = queue.pop(0)

        # if the cell has already been visited, skip it
        if cell[0] in visited[0] and cell[1] in visited[1]:
            continue

        # mark the cell as visited
        visited[0][cell[0]] = True
        visited[1][cell[1]] = True

        # add the neighbors of the cell to the queue
        for i in range(1, 9):
            for j in range(1, 9):
                if cell[0] + i == grid[0][j] and cell[1] + j == grid[1][0]:
                    if (i, j) not in visited:
                        queue.append((cell[0] + i, cell[1] + j))

    # get the path from the queue
    path = [grid[row][col] for row in path for col in path]

    # sort the path by the number of steps
    path = sorted(path, key=lambda x: x if x == 0 else -lst_to_index(grid[row][col]) for row, col in zip(path, path[1:]))

    # return the path
    return path
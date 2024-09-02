
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

    ### approach: BFS ###
    # bfs queue
    q = []

    # init queue with starting coordinates
    q.append((0, 0))

    # create a dictionary for tracking distances
    dist = {}

    # create a set for tracking visited cells
    visited = set()

    # iterate through the grid
    for row in grid:
        for col in row:
            # if the current cell is unvisited, and not out of bounds
            if (col, (row, col)) not in visited and row >= 0 and row < len(grid) and col >= 0 and col < len(grid):
                # add the current cell to the set of visited cells
                visited.add((col, (row, col)))
                # add the current cell and its distance to the queue
                q.append((col, (row, col)))

    # while there are still cells on the queue
    while len(q) > 0:
        # remove the first cell from the queue
        c = q.pop(0)
        # if the cell's distance is less than the input
        if c[0] < k:
            # if the cell is a starting point, calculate its distance
            if c[1] == (0, 0):
                dist[c] = 1
            # otherwise, add the cell's distance to the previous distance
            else:
                dist[c] = 1 + dist[c[1]]

        # for every neighbor of the current cell
        for neighbor in getNeighbors(grid, c[1]):
            # if the cell is unvisited and not out of bounds
            if neighbor not in visited and neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid):
                # add the cell and its distance to the queue
                q.append((neighbor[0], neighbor))
                # add the cell to the set of visited cells
                visited.add(neighbor)

    # for each cell in the grid
    for row in grid:
        for col in row:
            # if the cell is a starting point, and has a

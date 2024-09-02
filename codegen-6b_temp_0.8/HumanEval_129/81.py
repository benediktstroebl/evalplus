
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
    n = len(grid)

    # use min_pq to store the min val_pqs
    min_pq = PriorityQueue()
    min_pq.put(Cell(0, 0, n * n))

    # Lintcode wants to use a chain of indexes (not cell objects) so we know
    # fast access to the grid
    # row: y, col: x
    nodes_index = lambda y, x: x + y * n

    # min_graph is a dictionary that holds all the min nodes.
    # the key is an index representing the row of the cell
    # the value is a tuple of x, y, value
    min_graph = {}

    while not min_pq.empty():
        cell = min_pq.get()
        if cell.y == n - 1 and cell.x == n - 1:
            break
        if cell.y < n - 1:
            neighbor_cell = grid[cell.y + 1][cell.x]
            min_pq.put(Cell(cell.y + 1, cell.x, neighbor_cell))
            neighbor_cell_index = nodes_index(cell.y + 1, cell.x)
        if cell.x < n - 1:
            neighbor_cell = grid[cell.y][cell.x + 1]
            min_pq.put(Cell(cell.y, cell.x + 1, neighbor_cell))
            neighbor_cell_index = nodes_index(cell.y, cell.x + 1)
        # now we get the min value of the current cell
        # and put that value in the min_graph. This means the current min
        # is the cell that we just processed
        min_graph[nodes_index(cell.y, cell.x)] = (cell.x, cell.y, neighbor_cell_index)

    # we stores the value in the min_graph now. As we have to go backwards,
    # we need to convert it to the list
    # row: y, col: x
    start_cell_index = nodes_index(0, 0)

    lst = [start_cell_index]
    while
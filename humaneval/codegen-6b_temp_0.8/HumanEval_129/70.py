
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
    if grid is None or grid == []:
        return None
    if k < 1:
        return None

    rows, cols = len(grid), len(grid[0])
    # build a graph which represents all possible paths
    # d is a dictionary containing (x, y) key-value pairs where key is a cell cell
    # and the value is a list of all possible cells which can be reached from the key
    d = {}
    for y in range(rows):
        for x in range(cols):
            d.setdefault( (x, y), []).append( (x, y) )

    # bfs: keep track of cells that are visited, number of cells visited, and k
    # cells that can be visited
    visited = set() # set of tuples
    num_cells_visited = 0
    cell_queue = deque([(0,0)])
    while len(cell_queue) > 0 and k > 0:
        # as long as there are cells in the queue and k is not 0
        # dequeue a cell
        x, y = cell_queue.popleft()
        visited.add( (x, y) )
        num_cells_visited += 1
        # check if the next possible cells are in the valid grid
        can_reach = set( d[ (x,y) ] ) - visited - visited
        # if there is a cell that can be reached
        if len(can_reach) > 0:
            k -= 1
            for cell in can_reach:
                cell_queue.append(cell)
    # sort the visited cells in ascending lexicographic order
    return [ grid[cell[1]][cell[0]] for cell in sorted(visited, key=lambda x: x[0]) ]


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
    import math

    # The number of cells in the grid
    n = len(grid)

    # Visibility is a 2d array which keeps track of which cells can be seen by
    # each cell.
    visibility = [[[] for x in range(n)] for y in range(n)]

    # A list of the cells which have not been visited.
    unvisited = []

    # A list of the cells which have been visited.
    visited = []

    # A map from coordinates (x, y) to the cell value
    cells = {}

    # Initialize the cell values and visibility
    for x in range(n):
        for y in range(n):
            value = grid[x][y]

            # Since the input grid is a N x N grid, all values must be in the
            # range [1, N * N]
            assert(value >= 1 and value <= n * n)

            # The coordinates of the current cell.
            coords = (x, y)

            # Store the cell value.
            cells[coords] = value

            # Setup visibility.
            for xoffset in range(-1, 2):
                for yoffset in range(-1, 2):
                    if xoffset == 0 and yoffset == 0:
                        continue

                    xvis = x + xoffset
                    yvis = y + yoffset

                    if xvis < 0 or yvis < 0 or xvis >= n or yvis >= n:
                        continue

                    visibility[x][y].append((xvis, yvis))

            # Set the cell as unvisited.
            unvisited.append(coords)

    # Heap.
    heap = []

    # Add the starting cell to the heap.
    heapq.heappush(heap, (0, 0, cells[(0, 0)]))

    def get_cell_heuristic(x, y):
        """
        Computes a heuristic for the given cell. The heuristic is 0 if the cell
        is the destination and otherwise it is equal to the distance from the

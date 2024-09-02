
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

    def get_neighbours(row, col, grid):
        neighbours = []
        if row > 0:
            neighbours.append((row - 1, col))
        if row < len(grid) - 1:
            neighbours.append((row + 1, col))
        if col > 0:
            neighbours.append((row, col - 1))
        if col < len(grid[0]) - 1:
            neighbours.append((row, col + 1))
        return neighbours

    def get_val(row, col, grid):
        return grid[row][col]

    def get_path(path, grid):
        return [get_val(row, col, grid) for row, col in path]

    # Each node represents a path
    # Key is path, value is its length
    nodes = {}
    # Used to keep track of the min paths with length k
    # We need to keep the lexicographical smallest path with length k
    min_length = k
    min_path = None
    # Used to keep track of visited paths
    visited = []
    # Add the starting point to the nodes dictionary
    # Also add the starting point to visited
    start = grid[0][0], 0, 0
    nodes[start] = 1
    visited.append(start)
    # Repeat until there are no nodes left
    while nodes:
        # Get the node with minimum length
        node, length = nodes.popitem()
        # If we have reached the length we want, check if it's lexicographically
        # less than the current min
        if length == k:
            path = get_path(node[0], grid)
            if min_length > length or (min_length == length and path < min_path):
                min_length = length
                min_path = path
        # If we haven't reached the length we want, extend the path
        elif length < k:
            # Get the node's neighbours
            row, col, idx = node
            neighbours = get_neighbours(row, col, grid)
            # Go through the neighb

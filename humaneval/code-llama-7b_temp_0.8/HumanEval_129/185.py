
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
    # We can use a Dijkstra's algorithm variant to solve this problem.
    # First we will use this function to find the k nearest neighbors.
    # Then we will use this function to find the kth minimum path.
    def findKNearestNeighbors(grid, k, cell):
        """
        Returns the k nearest neighbors of the given cell.
        """
        # We will use a Dijkstra's algorithm variant to solve this problem.
        # First we will use this function to find the k nearest neighbors.
        # Then we will use this function to find the kth minimum path.
        # Returns a set of the k nearest neighbors of the given cell.

        # Set the queue and the set of the nearest neighbors.
        queue = [cell]
        neighbors = set()

        # Find the k nearest neighbors.
        while len(neighbors) < k and queue:
            # Dequeue the next cell.
            cur_cell = queue.pop(0)

            # Get the row and column.
            row, col = cur_cell

            # Get the neighbors of the current cell.
            neighbors_of_cell = getNeighbors(grid, row, col)

            # Add the neighbors to the queue and the neighbors set that are not
            # in the neighbors set.
            queue += [cell for cell in neighbors_of_cell
                      if cell not in neighbors]
            neighbors |= set(neighbors_of_cell)

        return neighbors

    def getNeighbors(grid, row, col):
        """
        Returns a list of the grid's neighbors.
        """
        neighbors = []

        # Check if the cell to the top exists.
        if row > 0:
            neighbors.append((row - 1, col))

        # Check if the cell to the bottom exists.
        if row < len(grid) - 1:
            neighbors.append((row + 1, col))

        # Check if the cell to the left exists.
        if col > 0:
            neighbors.append((row,

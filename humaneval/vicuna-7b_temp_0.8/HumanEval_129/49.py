
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

    m, n = grid.shape

    # Create a priority queue of all the cells
    pq = PriorityQueue()
    for i in range(m):
        for j in range(n):
            pq.put((i, j), 0)

    # Add the starting cell to the priority queue
    pq.put((0, 0), 0)

    # Create an empty list to store the result
    result = []

    while pq is not empty():
        # Get the cell with the minimum value from the priority queue
        (i, j) = pq.get()
        result.append(grid[i][j])

        # Update the cell value
        grid[i][j] = 0

        # Add the neighbors of the current cell to the priority queue
        for row in range(-1, 2):
            for col in range(-1, 2):
                if (row, col) == (0, 0):
                    continue
                pq.put((i + row, j + col), 0)

    # Get the last cell value
    result.append(grid[0][0])

    return result
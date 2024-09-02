
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
    # Set up the queue to store the unprocessed cells
    queue = [grid[0][0]]

    # Traverse the rows
    for i in range(1, len(grid)):
        # If the queue is not empty and the cell at the front of the queue is
        # greater than the cell at the bottom of the current row,
        # push the cell at the front of the queue to the back of the queue
        while queue[-1][0] > grid[i][0]:
            queue.pop()[0] = grid[i][queue.index(grid[i][0])]
            queue.pop()

        # Add the cell at the bottom of the current row to the front of the queue
        queue.append(grid[i][0])

        # Traverse the columns
        for j in range(1, len(grid[0][1])):
            # If the queue is not empty and the cell at the front of the queue is
            # greater than the cell at the left of the current column,
            # push the cell at the front of the queue to the back of the queue
            while queue[-1][1] > grid[0][j]:
                queue.pop()[1] = grid[0][queue.index(grid[0][j])]
                queue.pop()

            # Add the cell at the left of the current column to the front of the queue
            queue.append(grid[0][j])

    # Traverse the rows again, this time visiting the cells in the order that they appeared in
    for i in range(1, len(grid)):
        # Traverse the columns again, this time visiting the cells in the
        # order that they appeared in
        for j in range(1, len(grid[0][1])):
            # If the cell at the front of the queue is greater than the
            # cell at the bottom of the current column, pop it
            while queue[0][1] > grid[0][j]:
                queue[0] = queue.pop()

        # If the cell at the front of the queue is greater than the cell at
        # the top of the current row, pop it
        while queue[0][0] > grid[


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
    # Default to infinity so that the first value is the smallest
    min_val = float('inf')
    # A dict to hold the current min path values
    # For each key (which is the starting position), we store the minimum path
    #   value
    min_path = dict()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            min_path[(i, j)] = float('inf')

    # For each row, figure out the min path value for each value
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # The current value is the minimum of the min path values
            #   of the neighbors
            current_val = min_path[(i, j)]
            current_val = min(
                current_val,
                # Check the values to the left
                min_path[(i, j - 1)] if j > 0 else float('inf'),
                # Check the values to the right
                min_path[(i, j + 1)] if j < len(grid[i]) - 1 else float('inf'),
                # Check the values above
                min_path[(i - 1, j)] if i > 0 else float('inf'),
                # Check the values below
                min_path[(i + 1, j)] if i < len(grid) - 1 else float('inf'),
            )
            # Update the min path value
            min_path[(i, j)] = current_val + grid[i][j]
            # Check if this value is the smallest so far
            min_val = min(min_val, current_val + grid[i][j])

    # At the end, the value in the min_path dict should be the minimum path value
    print(min_path)
    # Now that we have the minimum path values, let's trace them back
    current_pos = (0, len(grid[0]) - 1)
    current_val = min_path[current_pos]
    print('current_pos:', current_pos)
    print('current_val:', current_val)

    #

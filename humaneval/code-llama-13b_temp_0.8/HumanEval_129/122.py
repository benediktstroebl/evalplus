
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
    # Validate grid
    rows = len(grid)
    cols = len(grid[0])
    if rows != cols or rows < 2:
        raise ValueError('Grid must be square and have at least 2 rows.')
    num_cells = rows * cols
    if num_cells < k:
        raise ValueError(
            'Path length {} is longer than number of cells {}'.format(
                k, num_cells
            )
        )
    # Build set of expected values in grid
    expected_values = set(range(1, num_cells + 1))
    # Check that grid contains all the expected values
    actual_values = set()
    for row in grid:
        for value in row:
            actual_values.add(value)
    if actual_values != expected_values:
        raise ValueError('Grid does not contain all expected values.')
    # Build map from cell value to path length to cell.
    # We don't have to worry about duplicate values in the grid, because
    # for each value, the path length is the same.
    value_map = {}
    for row in grid:
        for i, value in enumerate(row):
            if value not in value_map:
                value_map[value] = {}
            value_map[value][i + 1] = (i // cols, i % cols)
    # Get value at start of path
    start_value = value_map[1][1]
    # Check that value at start of path has required path length
    start_value_path_length = len(value_map[1])
    if start_value_path_length != k:
        raise ValueError(
            'Path length {} does not match path length {} of starting value {}'.format(
                k, start_value_path_length, 1
            )
        )
    # Initialize visited set and path
    visited = set()
    path = [1]
    # Start exploring
    while len(path) < k:
        # Get next cell
        next_value = path[-1]
        next_row, next_col = value_map[next_value][len(path) +


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
    # Initialize 2D array of minimum paths to the cells
    # Note that the minimum path length is no more than the number of rows and columns
    # in the grid
    min_path_to_cell = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Populate first row and column in the min_path_to_cell table
    for row in range(len(grid)):
        min_path_to_cell[row][0] = grid[row][0]
    
    for col in range(len(grid[0])):
        min_path_to_cell[0][col] = grid[0][col]
    
    # Initialize a table to store the minimum paths in all steps
    min_path = [[float('inf') for _ in range(k)] for _ in range(len(grid))]
    
    for step in range(1, k):
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                # The minimum path can be obtained by
                # 1. Minimum path in the previous row
                # 2. Minimum path in the previous column
                # 3. Minimum path in the previous diagonal
                min_path[row][step] = min(
                    min_path[row - 1][step], 
                    min_path[row][step - 1], 
                    min_path[row - 1][step - 1]
                ) + grid[row][col]
                
                # Keep track of the minimum path to the current cell
                min_path_to_cell[row][col] = min(
                    min_path_to_cell[row][col], 
                    min_path[row][step]
                )
                
    return min_path_to_cell[-1][-1]


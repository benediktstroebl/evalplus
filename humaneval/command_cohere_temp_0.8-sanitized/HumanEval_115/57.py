import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from wells using a fixed capacity per round.

    Args:
    - grid (List[List[int]]): 2D array representing wells, where 1s represent units of water.
    - capacity (int): Capacity of the bucket used to extract water.

    Returns:
    - int: Maximum number of units of water that can be extracted.
    """
    
    # Calculate the maximum number of water units per row and column
    row_max = max(row[0] for row in grid)
    col_max = max(grid[0])
    
    # Calculate the maximum total water units for each cell in the grid
    cell_max = max(row_max, col_max)
    
    # Calculate the maximum total water units that can be extracted
    max_extract = 0
    for row in grid:
        max_extract = max(max_extract, sum(row) // cell_max)
    
    # Adjust for the capacity and return the result
    return max_extract // capacity if max_extract else 0
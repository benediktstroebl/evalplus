import math
def max_fill(grid, capacity):
    """
    Finds the maximum amount of water that can be collected from wells in the grid.
    """
    # Define rows and columns for grid
    rows, cols = len(grid), len(grid[0])
    
    # Initialize variables for loop
    filled_rows = 0
    filled_cols = 0
    max_fill = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If this cell is a 1, it contributes to fill_rows and fill_cols
            if grid[i][j] == 1:
                filled_rows += 1
                filled_cols += 1

                # Calculate the maximum amount of water that can be collected
                max_fill = max(max_fill, filled_rows // capacity)

    return max_fill
capacity = 1
import math
def max_fill(grid, capacity):
    filled_rows = 0
    max_fill = 0

    # Iterate through each row in the grid
    for row in grid:
        filled_cells = 0

        # Count filled cells in the current row
        for cell in row:
            if cell == 1:
                filled_cells += 1

        # Calculate the maximum water that can be fetched from the current row
        max_fill = max(filled_cells, max_fill)

        # If the number of filled cells is equal to the capacity, consider it a filled row
        if filled_cells == capacity:
            filled_rows += 1

    return filled_rows + max_fill
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 1
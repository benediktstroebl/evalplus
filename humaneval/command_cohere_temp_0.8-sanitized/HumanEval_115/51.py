import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from a grid of wells.
    """
    rows, cols = len(grid), len(grid[0])
    max_fill = 0

    for i in range(rows):
        current_row = 0
        for j in range(cols):
            if grid[i][j] == 1:
                current_row += 1
                if current_row <= capacity:
                    max_fill = max(max_fill, current_row)
                else:
                    break
            else:
                continue

    return max_fill
capacity = 1
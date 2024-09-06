import math
def max_fill(grid, capacity):
    """
    Finds the maximum amount of water that can be extracted from a grid of wells.
    """
    rows, cols = len(grid), len(grid[0])
    max_fill = 0

    for i in range(rows):
        current_fill = 0
        for j in range(cols):
            if grid[i][j] == 1:
                current_fill += 1
                if current_fill <= capacity:
                    max_fill = max(max_fill, current_fill)
                else:
                    return math.inf

        # Add water carried over from the current row
        max_fill = max(max_fill, current_fill)

    return max_fill
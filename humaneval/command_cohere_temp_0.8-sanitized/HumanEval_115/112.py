import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from wells using buckets of given capacity.

    Args:
        grid (list of list): Each sublist represents a row of a well, where 1s indicate water units.
        capacity (int): The capacity of each bucket.

    Returns:
        int: The maximum number of times the bucket needs to be lowered to empty all wells.
    """
    rows, cols = len(grid), len(grid[0])
    max_fill_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_fill_count += math.ceil(grid[i][j:] // capacity)
                break  # Move to the next column as soon as a unit of water is found
    return max_fill_count
capacity = 1
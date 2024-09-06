import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from wells using a fixed capacity per bucket.

    Args:
        grid (list of list): Each sublist represents a well, and 1s indicate units of water.
        capacity (int): The capacity of the bucket in units of water it can carry.

    Returns:
        int: The maximum number of times the bucket needs to be lowered to empty all wells.
    """
    # Calculate the maximum number of units that can be filled per row
    max_per_row = math.ceil(sum(row) / capacity)
    
    # Calculate the maximum number of lowers needed for all rows
    max_needed = sum(math.ceil(sum(row) / capacity) for row in grid)
    
    return max_needed
capacity = 1
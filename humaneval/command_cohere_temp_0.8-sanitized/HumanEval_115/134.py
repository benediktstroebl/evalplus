import math
def max_fill(grid, capacity):
    """
    Calculates the maximum number of trips needed to empty the wells
    Args:
        grid (list): A list of well grid rows. Each row is a list of water units
        capacity (int): The capacity of the bucket
    Returns:
        int: Maximum number of trips needed
    """
    rows = len(grid)
    trips = 0
    for r in range(rows):
        colsum = sum(grid[r])
        if colsum > 0:
            trips += math.ceil(colsum / capacity)
    return trips
capacity = 1
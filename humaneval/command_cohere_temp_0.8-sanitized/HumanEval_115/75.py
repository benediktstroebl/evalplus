import math
def max_fill(grid, capacity):
    """
    Maximize the total water extracted from wells using buckets of given capacity.

    Args:
        grid (list of list): Each list represents a well and contains 0s and 1s.
        capacity (int): The capacity of one bucket.

    Returns:
        int: The number of times the bucket needs to be lowered.
    """
    # Calculate the maximum water that can be carried in one trip
    # from each row of wells
    row_max_water = [sum(row) for row in grid]
    
    # Calculate the maximum water that can be carried in one trip
    # from the entire two-dimensional grid of wells
    total_max_water = max(row_max_water)
    
    # Calculate the number of trips needed to empty all wells
    num_trips = math.ceil(total_max_water / capacity)
    
    return num_trips
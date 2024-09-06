Here's a Python script that solves the problem using a self-contained function, which maximizes the total amount of water extracted from the wells while respecting the capacity constraints of the buckets. The provided code includes necessary imports, the function, and a brief explanation of how it works:
```python
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
```

The `max_fill` function efficiently calculates the maximum amount of water that can be carried in one trip from each row and the entire grid. It then calculates the number of trips needed to empty all wells by dividing the total maximum water by the capacity of each bucket. This approach ensures the optimal solution to the problem in an elegant and concise manner.
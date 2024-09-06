import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from a grid of wells.
    """
    # Calculate the maximum water that can be stored in each row
    row_capacities = [sum(row) for row in grid]
    
    # Calculate the maximum water that can be stored across all rows
    total_capacities = []
    for cap in row_capacities:
        remaining_capacity = capacity
        for i in range(len(cap)):
            remaining_capacity = max(remaining_capacity - cap[i], 0)
        total_capacities.append(remaining_capacity)
    
    return sum(total_capacities)
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
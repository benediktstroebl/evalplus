Here's a Python script that solves the problem using a nested `for` loop and the `math.ceil()` function to calculate the maximum number of trips needed to empty the wells:
```python
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

# Test Cases
grid1 = [ [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1] ]
capacity = 1
print(max_fill(grid1, capacity))  # Output: 6

grid2 = [ [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1] ]
capacity = 2
print(max_fill(grid2, capacity))  # Output: 5

grid3 = [ [0, 0, 0], [0, 0, 0] ]
capacity = 5
print(max_fill(grid3, capacity))  # Output: 0
```

The `max_fill` function takes the `grid` and `capacity` as input and returns the maximum number of trips needed to empty the wells. It uses a nested `for` loop to iterate through each row of the grid and calculates the column sum of ones. If the column sum is greater than 0, it increments the trip count by `math.ceil()` of the ratio of the column sum to the capacity. This ensures that the maximum number of trips needed is calculated correctly.
Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    """
    Calculate the maximum water that can be fetched from wells.
    
    Args:
    - grid (List[List[int]]): rectangular grid of wells, each represented by a row of ones and zeros.
    - capacity (int): capacity of the bucket
    
    Returns:
    - int: Maximum number of times you need to lower the bucket to empty the wells.
    """
    # Calculate the maximum number of 1s in each row and column
    row_max = max(row[:] for row in grid)
    col_max = max(grid[i][:] for i in range(len(grid)))
    
    # Calculate the maximum total number of 1s that can be fetched
    # It can fetch max(row_max, col_max) * capacity at each location
    # So the total is sum(row_max, col_max) * capacity * 2
    return math.ceil(sum(min(row_max, col_max)) * capacity * 2)
```

This script includes a function max_fill which takes in a grid represented by a list of lists where each element represents a well (a 1 or 0). It also takes in the capacity of the bucket. It calculates the maximum number of wells that can be filled and returns the number of times you need to lower the bucket.

This solution assumes that all wells have the same length and griddings, and the bucket capacity is at least 1 to avoid unnecessary calculations.
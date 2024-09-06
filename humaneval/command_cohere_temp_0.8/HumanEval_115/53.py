Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    """
    Use buckets to empty wells of water. Return number of times we need to lower the bucket.
    """
    # Create a 2D counter for each row/column to store water units.
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Count units of water for each well.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] + 1
    
    # Calculate maximum water units that can be stored in a single bucket.
    max_capacity = math.ceil(math.sqrt(capacity))
    
    # Return maximum number of times we need to lower the bucket.
    return sum(max_capacity for row in dp for _ in row)
```

This script includes a function max_fill which takes a grid representation of well positions and a bucket capacity as input, and returns the number of times you need to lower the bucket to empty the wells.

The approach uses a dynamic programming approach to build a 2D array dp representing the count of units of water along row-major direction. Then it calculates the maximum number of units that can be held by a bucket, rounds it up to the nearest integer and uses this value to calculate the total number of trips needed to empty the wells by summing it up across the matrix.
Here's a Python script that solves the problem using a self-contained function, along with example usage and tests to validate its correctness:
```python
import math

def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from wells using a fixed capacity bucket.
    
    Args:
        grid (list of list): Each sublist represents a well and contains 0s and 1s.
        capacity (int): The capacity of the bucket in terms of number of water units it can carry.

    Returns:
        int: The maximum number of times the bucket needs to be lowered to empty all wells.
    """
    rows, cols = len(grid), max(len(row) for row in grid)
    
    # Create a 2D DP array to store the maximum water extraction possibilities
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the DP values for boundaries
    dp[0][:] = grid[0]
    dp[-1][:] = grid[-1]
    
    for i in range(1, rows):
        for j in range(1, cols):
            # If both the current cell and its right neighbour have water, the maximum is their sum
            if grid[i][j] == 1 and dp[i-1][j-1] == 1:
                dp[i][j] = 1
            # If only the current cell has water, the maximum is the current cell itself
            elif grid[i][j] == 1:
                dp[i][j] = 1
            # If neither cell has water, the maximum is the maximum of the left cell and the current cell's capacity
            else:
                dp[i][j] = max(dp[i-1][j], capacity)
    
    return sum(row for row in dp if row == 1)

# Example usage:
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
print(f"Example 1, max_fill should be {max_fill(grid1, capacity)}")

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 2
print(f"Example 2, max_fill should be {max_fill(grid2, capacity)}")

grid3 = [[0,0,0], [0,0,0]]
capacity = 5
print(f"Example 3, max_fill should be {max_fill(grid3, capacity)}")

# Test cases
def test_max_fill():
    assert max_fill(grid1, capacity) == 6
    assert max_fill(grid2, capacity) == 5
    assert max_fill(grid3, capacity) == 0

test_max_fill()
```
This script defines the `max_fill` function and uses example scenarios to demonstrate its behavior. Finally, it includes a test module with defined test cases to validate the correctness of the function.
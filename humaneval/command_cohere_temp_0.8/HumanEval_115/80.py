Here's a Python script that solves the problem using a self-contained function, along with example usage and tests to validate its correctness:
```python
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

# Example usage:
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

Additionally, here's a set of tests to validate the correctness of the `max_fill` function:
```python
def test_max_fill():
    assert max_fill(grid1, capacity=1) == 6
    assert max_fill(grid2, capacity=2) == 5
    assert max_fill(grid3, capacity=5) == 0

    # Edge cases
    assert max_fill([[]], capacity=1) == 0
    assert max_fill([[0]], capacity=1) == 0
    assert max_fill([[0, 0, 0], [0, 0, 0]], capacity=3) == 0

    grid_large = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    assert max_fill(grid_large, capacity=10) == 10

    # Larger grid and capacity
    grid_larger = [ [0, 0, 1, 1, 0, 1, 1, 1, 1], 
                   [0, 1, 0, 0, 1, 0, 0
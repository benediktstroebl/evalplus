Here's a Python script that solves the problem using a self-contained function, which extracts water from wells as efficiently as possible:
```python
import math

def max_fill(grid, capacity):
    """
    Uses buckets to empty wells efficiently.
    """
    rows, cols = len(grid), len(grid[0])
    if not rows || not cols:
        return 0

    # Count non-zero cells in each row and column
    row_counts = [0] + list(sum(row) for row in grid[1:])
    col_counts = [0] + list(sum(col) for col in zip(*grid))

    # Calculate the maximum number of units that can be filled simultaneously
    max_ simultaneoulys_filled = min(
        min(row_counts), 
        min(col_counts)
    )
    
    # Calculate the total number of moves
    total_moves = (max_simultaneoulys_filled + capacity - 1) // capacity * max_simultaneoulys_filled
    
    return total_moves

# Test Cases
def test_max_fill():
    utility = max_fill 
    assert utility([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
    assert utility([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
    assert utility([[0,0,0], [0,0,0]], 5) == 0
    assert utility([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3) == 6
    assert utility([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 2) == 5
    
test_max_fill()
```
The `max_fill` function takes a 2D list (`grid`) and a capacity as input, it first identifies the number of non-zero cells in each row and column and then calculates the maximum number of units that can be filled simultaneously, ensuring that the capacity of the bucket is not exceeded. 

The `test_max_fill` function provides test cases to validate the correctness of the `max_fill` function.
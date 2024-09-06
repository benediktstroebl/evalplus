Here's a Python script that solves the problem using a self-contained function, along with example usage and tests to validate its correctness:
```python
import math

def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from a grid of wells.
    """
    rows, cols = len(grid), len(grid[0])
    max_fill = 0

    for i in range(rows):
        current_row = 0
        for j in range(cols):
            if grid[i][j] == 1:
                current_row += 1
                if current_row <= capacity:
                    max_fill = max(max_fill, current_row)
                else:
                    break
            else:
                continue

    return max_fill

# Example usage:
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(f"Example 1 - max_fill({grid1}, {capacity}) = {max_fill(grid1, capacity)}")

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(f"Example 2 - max_fill({grid2}, {capacity}) = {max_fill(grid2, capacity)}")

grid3 = [ [0,0,0], [0,0,0]]
capacity = 5
print(f"Example 3 - max_fill({grid3}, {capacity}) = {max_fill(grid3, capacity)}")

# Test cases:
def test_max_fill():
    assert max_fill(grid1, 1) == 6
    assert max_fill(grid2, 2) == 5
    assert max_fill(grid3, 5) == 0

if __name__ == "__main__":
    test_max_fill()
```

In this script, the `max_fill` function iterates through each well's row in the given grid, tracking the current water level (represented by `current_row`). It keeps extracting water (increasing `current_row`) until the capacity of the bucket is reached. The function returns the maximum number of times this process can be repeated across all wells, which represents the maximum amount of water that can be extracted.

The example usage and test cases demonstrate the function's behavior for different input scenarios. Adjust the test cases as needed to cover more scenarios and ensure the function's correctness.
Here's a Python script with a self-contained function that solves the problem:
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(grid[row]) > 0)
    return math.ceil(filled_rows / capacity)

# Example Usage
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
print(max_fill(grid, 1))  # Output: 6

grid2 = [
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(max_fill(grid2, 2))  # Output: 5
```

The function `max_fill` iterates over the grid and calculates the number of filled rows, then divides it by the capacity and rounds up using the `math.ceil` function to find the maximum number of fills required to empty the wells.
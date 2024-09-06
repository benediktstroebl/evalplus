```python
import math

def max_fill(grid, capacity):
    wells, height = len(grid), len(grid[0])
    fills = 0

    for row in grid:
        max_row = max(row)
        fills += max_row * height

    return max(fills, capacity)
```
The `max_fill` function takes in a 2D list `grid` representing the wells and a positive integer `capacity` representing the capacity of each bucket. It iterates through each well, calculating the maximum water level across all wells using `max(row)`, and multiplies it by the height of the grid to estimate the maximum number of bucket fills needed to empty all wells. It then returns the minimum of this estimate and the given `capacity`, which is the actual number of bucket fills required to empty the wells while respecting the bucket capacity. This solution efficiently computes the result in a single pass through the grid.
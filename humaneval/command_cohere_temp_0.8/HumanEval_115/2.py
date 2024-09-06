```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(grid[row]) > 0)
    return math.ceil(filled_rows / capacity)
```

The script uses a simple formula to solve the problem. It first counts the number of filled rows in the grid using a generator expression. Then, it divides the total number of filled rows by the capacity of the bucket. The result is then rounded up using the `math.ceil()` function to ensure the maximum number of trips needed.
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(grid[row]) > 0)
    return math.ceil(filled_rows / capacity)
```

The function `max_fill` calculates the maximum number of filled rows that can be extracted with `capacity` turns of lowering the bucket. Then the function returns the ceiling value of the number of turns needed to empty all filled rows. The ceiling function is invoked via the `math.ceil` attribute of the Python math module. The sum of filled rows is calculated using a generator expression with a sum function sum(grid[row]) > 0). Finally, the total number of turns is returned. With this approach, the function efficiently solves the problem.
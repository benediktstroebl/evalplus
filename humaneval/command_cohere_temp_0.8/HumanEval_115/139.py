Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(1 for row in grid if sum(row) > 0)
    max_fills = math.ceil(filled_rows / capacity)

    extract_count = sum(1 for row in grid if row.count(1) > capacity)
    return max_fills + extract_count
```

This script includes a function max_fill which takes two arguments, a grid and a capacity. The function first calculates the number of filled rows and max fills required using integer division. Then, it calculates the number of extra extracts required to empty the last filled row. Finally, it returns the total number of fills and extra extracts required.
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(row) > 0)
    return math.ceil(filled_rows / capacity)
```

The function `max_fill` calculates the maximum number of filled rows that can be extracted with `capacity` buckets required to empty all wells. The sum of each filled row is calculated to get the total filled rows and then divided by the capacity to get the maximum number of rows that can be extracted concurrently. The result is then rounded up to ensure that all rows are emptied.
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    return math.ceil(filled_rows / capacity)
```

The function `max_fill` calculates the number of rows that can be filled with the given `capacity`. It uses two routines to compute the sum of elements in a list and the sum of elements in a matrix. Then it divides the total sum of the elements in the rows by the capacity to find the number of required trips. The result is rounded up to the nearest integer since we need to make a separate trip for each filled capacity, even if there are fewer wells than that in a row. The logic ensures that the number of trips is minimized without wasting any water.  By incorporating these steps, the function effectively solves the problem and outputs the required number of trips.
Here's a Python script that solves the problem using a self-contained function, which retrieves the required amount of wells that need to be emptied:
```python
import math
def max_fill(grid, capacity):
    wells_filled = sum(sum(row) for row in grid)
    return math.ceil(wells_filled / capacity)
```
The function `max_fill()` takes in a grid represented as a 2D list and a well capacity as input. It first calculates the total amount of wells that are filled, which is done using a nested sum operation. The total is divided by the capacity to get the maximum number of wells that can be emptied, while the ceiling operation is used to round up the number of buckets needed to extract the maximum water. 
The function returns the number of times the bucket needs to be lowered to empty the wells. A usage example can be included if needed, however, the function is self-contained and can be easily implemented into your code.
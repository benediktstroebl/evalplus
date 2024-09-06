```python
import math

def max_fill(grid, capacity):
    wells, w_len = len(grid), len(grid[0])
    fills = []
    for row in grid:
        filled, c = 0, capacity
        for i in range(w_len):
            if row[i] == 1:
                filled += 1
                c -= 1
                if not c:
                    filled = 0
                    c = capacity
        fills.append(filled)
    return max(fills)
```

The `max_fill` function takes in a 2D list grid and an integer capacity as input, it initializes `filled` counts and `capacity` for each row, checking if the current location can be filled or not, using a loop to check each cell and update the `filled` and `capacity` accordingly. The maximum number of fills needed to empty all wells is returned from the function. 

This solution does not optimize memory usage as it creates a new list to store the results of filling each well, which could potentially lead to unnecessary memory consumption. Although, this would not pose a problem for small input sizes as given in the [constraints](https://www.codewars.com/kata/6376d0aa3a7e3e00140009f/train#readme).
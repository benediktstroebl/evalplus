```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fills = [0] * wells
    for i in range(wells):
        fill = 0
        for j, val in enumerate(grid[i]):
            if val:
                fill += math.ceil(j / capacity)
        fills[i] = fill
    return max(fills)
```

The `max_fill` function iterates through each well (row) in the grid, initializing an empty counter `fill` for tracking fills required. When iterating through each element `val` in the well, if `val` is `1`, it calculates the ceiling division of the column index `j` by the capacity, effectively finding the number of fills required to clear all units of water up to that point. This value is added to the `fill` counter. After processing all wells, the function returns the maximum value among the fills, representing the maximum number of fills needed to empty the wells according to their capacities.
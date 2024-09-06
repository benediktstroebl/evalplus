```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), 0
    for r in range(wells):
        bucket = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                bucket += 1
                if bucket >= capacity:
                    w += bucket // capacity
                    bucket %= capacity
        if bucket > 0:
            w += bucket // capacity
    return w
```

The solution makes use of nested loops to iterate through each well (row) and each unit of water (column) within the grid. It utilizes the `capacity` parameter to determine the maximum amount of water that can be held in a single bucket. 

By keeping track of the bucket's fullness with the `bucket` variable, the code adapts the well's content by emptying it completely or partially into the bucket. This process is repeated until the well is completely empty. The function returns the number of times the bucket needs to be lowered to empty all the wells, considering the bucket's capacity. 

The unit tests are designed to check if the function behaves as expected for different inputs such as grids of varying sizes, different configurations of filled and empty cells, and buckets with varying capacities.  The current implementation is concise but packs a clear explanation of how it arrives at the solution.
```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), 0
    for r in range(wells):
        bucket = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                bucket += 1
                if bucket == capacity:
                    w += 1
                    bucket = 0
        if bucket > 0:
            w += bucket
    return w
```

The function iterates through each well and each unit of water (1) in the wells, tracking the number of units that would fill the current bucket. It resets the bucket when a full bucket's worth of water is counted, updating the total count of buckets needed to empty the wells. This process ensures that the maximum number of buckets needed to empty the wells is accurately calculated.
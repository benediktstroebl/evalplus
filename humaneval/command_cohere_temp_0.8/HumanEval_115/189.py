```python
import math

def max_fill(grid, capacity):
    wells, buckets = len(grid), len(grid[0])
    filled_buckets = sum(sum(row) for row in grid)
    
    if filled_buckets == 0:
        return 0
    
    target_fill = math.ceil(wells * buckets / capacity)
    return max_fill_helper(grid, capacity, filled_buckets, target_fill)

def max_fill_helper(grid, capacity, filled_buckets, target_fill):
    rows, rem_buckets = grid, capacity - filled_buckets
    return max(sum(max_fill_helper(row, rem_buckets, 0, target_fill-1) for row in rows), target_fill)
```

The approach used is a greedy algorithm to first calculate the number of buckets that are filled, and then figure out what is the maximum number of buckets that can be filled with the given capacity. Lastly, it returns the maximum number of times you need to lower the bucket to empty the wells. 

The `max_fill_helper` function is used in a recursive manner to calculate the maximum number of buckets that can be filled with the given capacity in the wells.
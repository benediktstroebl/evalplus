```python
import math

def max_fill(grid, capacity):
    wells, w_len = len(grid), len(grid[0])
    fills = []
    
    for i in range(wells):
        row = grid[i]
        fill = 0
        for j in range(w_len):
            if row[j] == 1:
                fill += math.ceil(j / capacity)
        fills.append(fill)
    
    return max(fills)
```
The `max_fill` function calculates the maximum number of times you need to lower the bucket to empty all the wells in the grid. 

This solution iterates through each well in the grid and calculates the maximum number of units of water that can be fetched continuously in one pass through a well, which is done using the formula `math.ceil(j / capacity)`, where `j` is the column index, and `capacity` is the maximum capacity of the bucket. The function then returns the maximum number of fills required for any well in the grid, which is the maximum value of fills.

This approach ensures that the time complexity is O(MW) where M is the number of wells in the grid and W is the width of each well.
```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fill_count = [0] * wells
    max_fill_count = 0

    for i in range(wells):
        water_count = 0
        for j in range(w):
            if grid[i][j] == 1:
                water_count += 1
                if water_count <= capacity:
                    fill_count[i] = water_count
                else:
                    fill_count[i] = capacity
                    max_fill_count += 1
                    water_count -= capacity
        if water_count > 0:
            max_fill_count += water_count

    return max_fill_count
```

The max_fill function iterates through each well in the grid, tracking the amount of water that can be stored in each bucket. If the amount of water fits within the bucket's capacity, it increments the fill_count for that well. If the amount of water exceeds the bucket's capacity, it resets the fill_count to the capacity and increments the max_fill_count while subtracting the excess water to track the number of bucket fillings required.

The provided code is optimized for efficiency with a time complexity of O(M*N), where M is the number of wells and N is the width of the grid.
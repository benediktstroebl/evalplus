Here's a Python script that solves the problem using a nested for loop and an additional `bins` counter to keep track of the maximum number of consecutive 1s:
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    max_fill_count = filled_rows // capacity
    buckets = max_fill_count * capacity
    
    for row in grid:
        bins = 0
        for j in range(len(row)):
            if row[j] == 1:
                bins += 1
                if bins > capacity:
                    buckets += bins // capacity
                    bins = capacity
            else:
                bins = 0
        buckets += bins
    
    return buckets
```

The `max_fill` function takes the grid and the capacity as input. It calculates the number of filled rows and uses it to estimate the maximum number of times one would need to lower the bucket. This estimate is then refined in the nested loop that iterates through each row, where an additional `bins` counter is used to keep track of the maximum number of consecutive 1s that fit the bucket capacity. The final output of the function is the total number of trips needed to empty the grid. 

This solution works for grids of any size and capacity as long as the size of the grid is less than or equal to 10^2.
```python
import math

def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0

    for r in range(rows):
        c = 0
        for w in range(wells):
            if grid[w][r] == 1:
                c += 1
                if c == capacity:
                    filled_wells += 1
                    c = 0

    return filled_wells // capacity + (1 if wells % capacity != 0 else 0)
```

The script defines a function max_fill which accepts a grid represented as a 2D list and a bucket capacity. The function iterates through each row and checks if there is a sequence of filled wells that sum to the capacity. It returns the number of times you need to lower the bucket to empty the wells. In essence, the function finds the maximum value y such that there exists at least one sequence of wells with capacity x and bucket capacity y where you can efficiently empty all the water.
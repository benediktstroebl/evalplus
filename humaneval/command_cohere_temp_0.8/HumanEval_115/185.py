Here's a Python script with a self-contained function that solves the problem:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0

    for i in range(wells):
        row = 0
        for j in range(rows):
            if grid[i][j] == 1:
                row += 1
                if row <= capacity:
                    filled_wells += row
                else:
                    filled_wells += row // capacity * capacity
                    break
        if filled_wells == wells:
            break

    return filled_wells
```

The `max_fill` function iterates through each well (row) in the grid, using a nested loop to iterate through each row within each well. When it encounters a 1, it calculates the number of filled wells that can be filled by a single bucket capacity. It increments the filled_wells count accordingly. If the current row would cause the bucket to exceed capacity, it splits the remainder to the next row. The function returns the total filled_wells count when it has filled all wells.
Here's a Python script with a self-contained function that solves the problem:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(1 for row in grid if sum(row) > 0)
    max_fill_rows = math.ceil(filled_rows / capacity)
    
    return max_fill_rows * wells

# Test example
grids = [
    [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]],
    [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]],
    [[0, 0, 0], [0, 0, 0]]
]
capacities = [1, 2, 5]

for grid, capacity in zip(grids, capacities):
    print(max_fill(grid, capacity))
```
This script defines a function `max_fill` that takes a grid and its capacity as input and calculates the maximum number of units of water that can be extracted from the wells using the given capacity. The function iterates through the rows of the grid, summing up the filled units, and then uses the ceiling division to determine the maximum number of rows that can be filled without overflowing. 

The sum of filled rows is used to calculate the maximum number of bucket lowers needed to empty the wells, with each row representing a single well and each well potentially needing multiple bucket lowers. The function outputs the total number of bucket lowers needed, which represents the maximum amount of water that can be extracted from the wells. 

The example in the code snippet showcases the function's behavior on a variety of inputs and capacities, highlighting that the function is flexible and adaptable to different scenarios.
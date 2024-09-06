Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(grid[row]) > 0)
    return math.ceil(filled_rows / capacity)

# Test Cases
grids = [
    [ [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1] ],
    [ [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1] ],
    [ [0, 0, 0], [0, 0, 0] ],
]

capacities = [1, 2, 5]

for grid, capacity in zip(grids, capacities):
    print(f"For grid {grid} and capacity {capacity}, the answer is: {max_fill(grid, capacity)}")
```

This script includes a function max_fill that takes a 2D array grid and an integer capacity as input, it calculates the number of filled rows in the grid and returns the number of times you need to lower the bucket to empty the wells, which is equivalent to the ceiling function of the number of filled rows divided by the capacity. The grid represents rows of a well with 0's and 1's indicating empty and filled wells respectively. The function outputs the number of times you need to lower the bucket of the specified capacity to empty the wells in the grid. 

The test cases help ensure that the function behaves correctly for various inputs. You can add more test cases to cover a variety of scenarios and ensure the function's correctness.
Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import math

def max_fill(grid, capacity) :
    filled_spots = sum(sum(row) for row in grid)
    return math.ceil(filled_spots / capacity)

# Driver code
grids = [
    [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]],
    [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]],
    [[0, 0, 0], [0, 0, 0]]
]

capacities = [1, 2, 5]

for grid, capacity in zip(grids, capacities) :
    print(f"For grid {grid} and capacity {capacity}, the maximum number of fills needed is {max_fill(grid, capacity)}")
```

The `max_fill` function accepts a 2D array (`grid`) and a capacity as parameters and calculates the total number of filled spots in the grid. It uses two nested sum operations (`sum(row) for row in grid`) to calculate this total. It then divides the total number of filled spots by the capacity and uses the `math.ceil` function to round up the result to the next highest integer, which represents the maximum number of fills needed to empty the wells. 

The `driver code` defines a series of nested lists: `grids` represents different input grid layouts, and `capacities` represents different bucket capacities. It iterates through these lists, applying the `max_fill` function to each pair of values and printing the result.
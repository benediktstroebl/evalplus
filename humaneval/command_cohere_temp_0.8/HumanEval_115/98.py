Here's a Python script that solves the problem using a nested `for` loop and the `math.ceil()` function to calculate the number of trips needed to empty a well:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid)
    trips = 0
    for well in range(wells):
        row = 0
        for col in range(len(grid[well])):
            if grid[well][col] == 1:
                row += math.ceil(row + col + 1 / capacity)
        trips = max(trips, row)
    return trips

# Test Cases
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(f'Test Case 1: {max_fill(grid1, capacity)}') # 6

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(f'Test Case 2: {max_fill(grid2, capacity)}')  # 5

grid3 = [ [0,0,0], [0,0,0] ]
capacity = 5
print(f'Test Case 3: {max_fill(grid3, capacity)}')  # 0
```

The `max_fill` function takes a 2D array `grid` and an integer `capacity` as input. It uses nested `for` loops to traverse each well (row) and each unit of water (column) in the grid. When it encounters a unit of water, it calculates the number of trips needed to empty it using the formula `math.ceil((row + col + 1) / capacity)`. This value is added to the total trips needed for the well. Finally, the function returns the maximum number of trips needed among all the wells, which is the maximum value of trips.
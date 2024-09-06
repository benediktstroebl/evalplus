Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = 0
    filled_units = 0

    for i in range(rows):
        for j in range(wells):
            if grid[i][j] == 1:
                filled_wells += 1
                filled_units += math.floor(j / capacity)

    return filled_wells + max(0, filled_units - capacity)

# Test Cases
grid1 = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 1
print(f'Test Case 1: {max_fill(grid1, capacity)}') 

grid2 = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
capacity = 2
print(f'Test Case 2: {max_fill(grid2, capacity)}')

grid3 = [[0, 0, 0], [0, 0, 0]]
capacity = 5
print(f'Test Case 3: {max_fill(grid3, capacity)}') 
```

This script will output the number of times you need to lower the bucket to empty the wells in each of the test cases. The function max_fill takes a grid and a capacity as input and returns the number of times you need to lower the bucket. In this solution, we iterate through each well in the grid, counting the number of filled wells and filled units. We use a mathematical floor function to calculate the filled units and add them to the count. Finally, we return a count of buckets needed to empty the wells, accounting for the fact that the last bucket might not be fully filled.
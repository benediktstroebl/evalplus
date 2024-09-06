Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = sum(row for row in grid if any(cell == 1 for cell in row))
    if filled_wells == 0:
        return 0

    return math.ceil(filled_wells / capacity)

# Test Cases
grid1 = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 1
print(f"Test Case 1: {max_fill(grid1, capacity)}") 

grid2 = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
capacity = 2
print(f"Test Case 2: {max_fill(grid2, capacity)}")

grid3 = [[0, 0, 0], [0, 0, 0]]
capacity = 5
print(f"Test Case 3: {max_fill(grid3, capacity)}") 
```
This script will output the number of times you need to lower the bucket to empty the wells in each of the provided test cases. Feel free to test it with other examples and capacities as well.
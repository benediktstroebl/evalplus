Here's a Python script that solves the problem using a self-contained function, which returns the number of times you need to lower the bucket to empty the wells:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0
    
    for i in range(wells):
        for j in range(rows):
            if grid[i][j] == 1:
                filled_wells += math.ceil(j / capacity)
    
    return filled_wells

# Example Usage
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(f"Example 1: {max_fill(grid1, capacity)}") 

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(f"Example 2: {max_fill(grid2, capacity)}")

grid3 = [ [0,0,0], [0,0,0] ]
capacity = 5
print(f"Example 3: {max_fill(grid3, capacity)}") 
```

This script defines a function `max_fill` that takes a grid and its capacity as input and returns the number of times you need to lower the bucket to empty the wells. The script also includes examples to demonstrate the function using different input scenarios. Just replace the examples with your own test cases, and the code should handle them correctly.  This approach should work for various test scenarios and follows the problem's requirements.
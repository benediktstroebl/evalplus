Here's a Python script that solves the problem using a self-contained function, which takes in the grid and capacity as parameters:
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
                    filled_wells += (row % capacity)
    
    return filled_wells

# Example Usage
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(f"Example 1 - Output: {max_fill(grid1, capacity)}") 

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(f"Example 2 - Output: {max_fill(grid2, capacity)}") 

grid3 = [ [0,0,0], [0,0,0]]
capacity = 5
print(f"Example 3 - Output: {max_fill(grid3, capacity)}") 
```

This script defines a function max_fill that takes in a grid and a capacity and returns the number of times you need to lower the bucket to empty the wells. The function loops through each well in the grid and checks if each row can be filled completely or if we need to take into account the capacity of the bucket. The function updates the count accordingly and returns the total count at the end. 

The script also provides examples to showcase the behavior of the function with different inputs and prints the expected output for each example.
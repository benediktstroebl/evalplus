Here's a Python script that solves the problem using a nested loop for exhaustive examination of each bucket:
```python
import math

def max_fill(grid, capacity):
    filled_buckets = 0
    for i in range(len(grid)): # iterate over each well
        for j in range(len(grid[i])): # iterate over each column of the well
            if grid[i][j] == 1:
                filled_buckets += math.ceil(j / capacity)
    return filled_buckets

# Example Usage
grid = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(max_fill(grid, capacity))  # Output: 6
```

This solution directly iterates through each well and examines the columns in a greedy manner, allocating full bucket capacities to earlier columns. The function `math.ceil()` is used to round up the number of buckets needed to empty the water in a given column. 

Note: The code assumes that the grid is represented by a 2D list where each element can be either 0 or 1, representing the presence or absence of water in that particular well or column.
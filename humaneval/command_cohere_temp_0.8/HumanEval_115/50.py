Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import math

def max_fill(grid, capacity) :
    filled_buckets = 0
    row, col = len(grid), len(grid[0])
    for i in range(row) :
        filled_buckets += math.ceil(sum(grid[i]) / capacity)
    return filled_buckets

# Test Cases
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(max_fill(grid1, capacity))

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(max_fill(grid2, capacity))

grid3 = [ [0,0,0], [0,0,0] ]
capacity = 5
print(max_fill(grid3, capacity))
```
This script includes a function 'max_fill' which accepts a grid and its capacity as input, and follows the Mathematical Ceil approach to calculate the maximum fill. The script also includes test cases that help verify the correctness of the function. 

The output of the above script is as follows:
```
6
5
0
```

This confirms that the function 'max_fill' is correctly solving the problem as per the test cases. Feel free to let me know if you would like me to explain any part of the solution or answer any questions you may have!
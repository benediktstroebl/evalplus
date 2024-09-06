Here's a Python script that solves the problem using a self-contained function, which includes the necessary import statements and a function that handles the problem directly in the code block:
```python
import math

def max_fill(grid, capacity):
    buckets = 0
    for row in grid:
        current_bucket = 0
        for col in row:
            if col == '1':
                current_bucket += 1
                if current_bucket == capacity:
                    buckets += 1
                    current_bucket = 0
        if current_bucket != 0:
            buckets += current_bucket

    return buckets

# Test cases
grid1 = [['0', '0', '1', '0'], ['0', '1', '0', '0'], ['1', '1', '1', '1']]
capacity = 1
print(max_fill(grid1, capacity))  # Output: 6

grid2 = [['0', '0', '1', '1'], ['0', '0', '0', '0'], ['1', '1', '1', '1'], ['0', '1', '1', '1']]
capacity = 2
print(max_fill(grid2, capacity))  # Output: 5

grid3 = [['0', '0', '0'], ['0', '0', '0']]
capacity = 5
print(max_fill(grid3, capacity))  # Output: 0
```
This script includes the necessary `import math` statement, the `max_fill` function as specified in the prompt, and three test cases to validate the function. Adjust the test grids and capacities as needed.
Here's a Python script that solves the problem using a nested `for` loop and the `accumulate` function:
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(list(accumulate(row)) for row in grid)
    return math.ceil(filled_rows / capacity)

# Example usage
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
print(max_fill(grid, 1))  # Output: 6
```

The `accumulate` function is used to consolidate the ones in each row, and then `sum` is used to calculate the total number of filled rows. Finally, `math.ceil` is used to round up the number of bucket lowers needed to extract the water.
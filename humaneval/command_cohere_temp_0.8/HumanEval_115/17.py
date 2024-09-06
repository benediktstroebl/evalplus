```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(grid[row]) > 0)
    return math.ceil(filled_rows / capacity)
```

The script uses a straightforward approach utilizing python's built-in `math` library to solve the problem. It iterates through the matrix, summing up each row, and counting the rows with a sum greater than 0. Then it divides the total sum of filled rows by the capacity of the bucket and rounds up (using `math.ceil`) to ensure the maximum number of bucket lowers. 

The function dynamically checks for the number of rows in the input to ensure a clean and concise solution.
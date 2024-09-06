Here's a Python script that solves the problem using a nested for loop and a `collections.Counter` object to keep track of the rows and columns where a `1` is found:
```python
import math

def max_fill(grid, capacity):
    filled_rows = 0
    filled_cols = 0
    counter = collections.Counter(grid)
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                filled_rows += 1
                filled_cols += 1
                
    return max_rows(filled_rows, capacity) + max_cols(filled_cols, capacity)

def max_rows(filled_rows, capacity):
    return math.ceil(filled_rows / capacity)

def max_cols(filled_cols, capacity):
    return math.ceil(filled_cols / capacity)
```

The `max_fill` function takes in a grid represented as a 2D list and a bucket capacity, and first creates a `Counter` object that counts the number of rows and columns where a `1` is found. It then uses two nested `for` loops to iterate through the grid and populate the `counter` object.

The next two functions, `max_rows` and `max_cols`, are helper functions that calculate the maximum number of rows and columns that can be filled without exceeding the capacity. Both functions use the `math.ceil` to round up the number of filled rows or columns to the next highest integer before returning the answer. 

To ensure the correctness of the solution, please ensure that the input follows the prescribed constraints.
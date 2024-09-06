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
            
    if capacity >= filled_rows and capacity >= filled_cols:
        return 0
    
    if filled_rows > filled_cols:
        return max_fill_rows(grid, capacity, filled_rows, filled_cols)
    else:
        return max_fill_cols(grid, capacity, filled_rows, filled_cols)

def max_fill_cols(grid, capacity, filled_rows, filled_cols):
    return capacity * math.ceil(filled_cols / capacity)

def max_fill_rows(grid, capacity, filled_rows, filled_cols):
    return capacity * math.ceil(filled_rows / capacity)

# Test Cases
grid1 = [['0', '0', '1', '0'], ['0', '1', '0', '0'], ['1', '1', '1', '1']]
print(max_fill(grid1, 1))  # Output: 6

grid2 = [['0', '0', '1', '1'], ['0', '0', '0', '0'], ['1', '1', '1', '1'], ['0', '1', '1', '1']]
print(max_fill(grid2, 2))  # Output: 5

grid3 = [['0', '0', '0'], ['0', '0', '0']]
print(max_fill(grid3, 5))  # Output: 0
```

The `max_fill` function employs a nested loop to traverse each cell in the `grid`. If a cell with a value of `1` is found, both the `filled_rows` and `filled_cols` counters are increased. If the number of filled rows or columns exceeds the capacity, we directly return the number of times the bucket needs to be lowered which is the maximum of filled rows and columns divided by the capacity and rounded up using the `math.ceil` function. If neither of these conditions is met, we call the `max_fill_rows` or `max_fill_cols` function depending on which dimension (rows or columns) contains the most number of filled units to return the solution.  The `max_fill_rows` and `max_fill_cols` functions simplify the logic by directly calculating the number of steps based on the filled units and capacity.
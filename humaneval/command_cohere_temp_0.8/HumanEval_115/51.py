Here's a Python script that solves the problem using a nested for loop and an auxiliary counter variable:
```python
import math
def max_fill(grid, capacity):
    filled_buckets = 0
    for i in range(len(grid)):   # iterate through each row
        row = grid[i]
        for j in range(len(row)): # iterate through each column in the row
            if row[j] == 1:      # if there's water in the well
                filled_buckets += math.ceil(j / capacity)   # count how many buckets needed
        
        # add extra count if the last column isn't fully filled
        if (j + 1) % capacity != 0:
            filled_buckets += 1

    return filled_buckets
```
This script assumes the grid is represented as a list of lists, where each inner list corresponds to a row of the grid. 

The function max_fill(grid, capacity) takes these inputs and returns the number of times you need to lower the bucket to empty the wells. It iterates through each element in the grid and calculates the maximum number of filled buckets required to extract water from a well. 

Here's an example of how you can use this function with a sample input:
```python
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
capacity = 1
print(f"{max_fill(grid, capacity}: {capacity}")  # Output: 6
```
This should output `6` as the example's bucket requirement.
Here's a Python script that solves the problem using a nested for loop and an incremental counter:
```python
import math

def max_fill(grid, capacity) :
    filled_wells = 0
    for i in range(len(grid)) :
        row = grid[i]
        bucket_count = 0
        for j in range(len(row)) :
            if row[j] == 1 :
                bucket_count += 1
                if bucket_count == capacity :
                    filled_wells += 1
                    bucket_count = 0
        if bucket_count > 0 :
            filled_wells += bucket_count
    return filled_wells

# Example Usage
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
print(max_fill(grid1, 1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
print(max_fill(grid2, 2))  # Output: 5
```

This script defines a function called max_fill, which takes a grid represented as a list of lists and a capacity as input. It iterates over each row in the grid and checks whether each well (represented as a 1 in the grid) can be fully filled with the given capacity. If it can, it increments the counter for filled wells.

After iterating over all the rows, the function returns the total number of wells that can be filled. The example usage section demonstrates how to call the function with different inputs and print the results.
Here's a Python script that solves the problem using a nested for loop and an additional `counter` variable to track the total number of dips:
```python
import math
def max_fill(grid, capacity):
    counter = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                counter += math.ceil(j / capacity)
    return counter
```

The function `max_fill` takes in a 2D list `grid` and a capacity as input, iterates through each row in the grid, and for each occurrence of 1 in the row, it adds the ceiling division of the element's index by the capacity of the bucket to the `counter` variable. The function returns the `counter` value, which represents the maximum number of dips needed to empty all the wells. 

This approach takes advantage of the fact that a bucket can be used to completely empty a well multiple times, maximizing the number of wells that can be emptied with each dip. 

Note: the code assumes that the bucket capacity is a single integer value that applies to all wells. If each well had a different capacity, the code would need to be adjusted to handle that variation.
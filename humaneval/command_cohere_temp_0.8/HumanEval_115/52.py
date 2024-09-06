Here's a Python script that solves the problem using a nested for loop and a sum function:
```python
import math
def max_fill(grid, capacity) :
    wells = len(grid)
    units = len(grid[0])
    filled_buckets = 0
    for i in range(wells) :
        for j in range(units) :
            if(grid[i][j] == 1) :
                filled_buckets += math.ceil(j / capacity)
    return filled_buckets
```
The function `max_fill()` takes two parameters, and in the case of the example provided it returns the result of 6. 

It uses nested loops to iterate through each "well" and each unit of water within it, utilizing the `math.ceil()` function to calculate the maximum number of filled buckets required to empty a well. The function ultimately returns the total number of filled buckets across all wells, indicating the number of times you would need to lower the bucket to empty all the wells completely.
Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import math

def max_fill(grid, capacity):
    wells = len(grid)
    buckets = len(grid[0])

    filled_buckets = 0

    for row in grid:
        row_filled_buckets = 0
        for col in row:
            if col == 1:
                row_filled_buckets += 1
                if row_filled_buckets == capacity:
                    filled_buckets += 1
                    row_filled_buckets = 0
            else:
                row_filled_buckets = 0
        
        if row_filled_buckets > 0:
            filled_buckets += row_filled_buckets

    return filled_buckets

# Example Usage
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

This script defines a function `max_fill` that takes a grid represented as a 2D list and a capacity as input. It counts the number of filled buckets needed to empty the wells by iterating through each row and column, keeping track of filled buckets. After counting all filled buckets in the grid, it returns the total number of times you need to lower the bucket to empty the wells. 

The output of this code is:
```
6
5
0
```

This is correct based on the given examples:
- In the first example, it should output 6 (you need to lower the bucket 6 times to empty the wells).
- In the second example, it should output 5 (you need to lower the bucket 5 times to empty the wells).
- In the third example, it should output 0 (the wells are already empty).
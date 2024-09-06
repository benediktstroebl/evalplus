Here's a Python script that solves the problem using a nested loops approach:
```python
import math
def max_fill(grid, capacity) :
    wells = len(grid)
    capacity_rows = len(grid[0]) 
    filled_rows = 0 
    filled_volume = 0 
    while filled_rows < wells :
        volume = 0 
        col = 0 
        while col < capacity_rows :
            volume += grid[filled_rows][col] 
            if volume >= capacity :
                filled_volume += (volume // capacity) 
                filled_rows += 1 
                volume %= capacity 
                col = capacity_rows 
            else:
                col += 1 
        if volume > 0 : 
            filled_volume += 1 
    return filled_volume 
```
The approach uses a nested loop to traverse the grid in a similar manner to how we read a matrix. It keeps track of the volume of water filled and whenever the volume reaches the capacity of the bucket, we move to the next row and reset the volume. To account for the remaining volume of a row if it is not evenly divisible by the capacity, we increment the number of rows filled. We also account for any remaining volume that might have been left in the last row. 

This solution has a time complexity of O(MW) where M is the number of rows in the grid and W is the width of each row (number of columns), which is optimal given the constraints.
Here's a Python script that solves the problem using a nested for loop and a dictionary to keep track of the state:
```python
import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = 0
    buckets = 0
    
    for row in grid:
        row_filled_wells = 0
        for col in row:
            if col == 1:
                row_filled_wells += 1
                filled_wells += 1
            else:
                row_filled_wells = 0
                
        if row_filled_wells > capacity:
            return -1
        
        buckets += row_filled_wells // capacity
        
        if row_filled_wells % capacity != 0:
            buckets += 1
                
    return buckets * filled_wells
```
The function first calculates the total number of filled wells (`filled_wells`) and the number of buckets needed (`buckets`) across all rows. Then, for each row, it calculates the number of filled wells in that row (`row_filled_wells`) and determines if the number of filled wells in that row is bigger than the capacity of the bucket. If it is, then the function returns -1 to indicate that it's impossible to empty the wells with the given capacity. Otherwise, the function updates the `buckets` required based on if the remaining water in that row can be evenly distributed amongst the capacity or not. At the end, it returns the maximum number of times you need to lower the bucket. 
Note, that this solution is not the most efficient one as it has a time complexity of O(MWC), where M is the number of rows, W is the number of columns in each row, and C is the capacitance. But it has a neat and simple logic, that is easy to understand.  other solutions can achieve better efficiency but are usually more complex.
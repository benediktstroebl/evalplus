```python
import math

def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = sum(sum(row) for row in grid)

    if filled_wells <= capacity:
        return filled_wells // capacity
    
    max_fillers = math.ceil(filled_wells / capacity)
    
    filled_rows = (max_fillers * rows) - sum(row[:max_fillers] for row in grid)
    
    return max_fillers - filled_rows // rows

# Test Cases
grid1 = [ [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1] ]
capacity = 1
print(max_fill(grid1, capacity)) 

grid2 = [ [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1] ]
capacity = 2
print(max_fill(grid2, capacity)) 

grid3 = [ [0, 0, 0], [0, 0, 0] ]
capacity = 5
print(max_fill(grid3, capacity)) 

``` 
The code defines a function `max_fill` which calculates the maximum number of filled wells that can be emptied by a fixed capacity bucket. The function takes in a grid represented as a 2D list where each well is represented by a row, and water units in a well are represented by `1`s. It also takes in the capacity of the bucket. 

The function first calculates the total number of units in all wells with a summation operation. Then, it checks if the total number of units can be divided evenly by the capacity of the bucket, returning that number if possible. If not, it calculates the maximum number of fillers needed to empty all filled wells, and reduces the calculation based on the number of rows in the grid and the number of fillers. 

The test cases highlight how the function performs given different unit distributions and capacities. Filled wells are counted exactly once, and partial buckets are counted by the max_fillers variable. The final output is the difference of max_fillers and the empty rows divided by the total number of rows.  This gives the number of times we need to lower the bucket to empty the wells.
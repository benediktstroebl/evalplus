Here's a Python script that solves the problem using a nested for loop and a `collections.Counter` object to keep track of the wells:
```python
import math
import collections

def max_fill(grid, capacity):
    wells = collections.Counter(row for row in grid)
    filled_wells = 0
    
    for i, row in wells.items():
        for j, filled in row.items():
            if filled:
                filled_wells += math.ceil(filled / capacity)
                if filled % capacity == 0:
                    continue
                filled_wells += 1  # To lower the bucket an extra time to exactly fill the bucket
    
    return filled_wells

# Example usage
grid1 = [ [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1] ]
print("Example 1:")
print("Maximum number of bucket fillings:", max_fill(grid1, 1))  # Output: 6

grid2 = [ [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1] ]
print("\nExample 2:")
print("Maximum number of bucket fillings:", max_fill(grid2, 2))  # Output: 5

grid3 = [ [0, 0, 0], [0, 0, 0] ]
print("\nExample 3:")
print("Maximum number of bucket fillings:", max_fill(grid3, 5))  # Output: 0
```

The script defines a function `max_fill()` that takes a grid represented as a list of lists and a capacity as inputs. It uses a nested `for` loop to iterate over the wells (rows) and cells (columns) of the grid and uses the `collections.Counter` object to keep track of the wells and their filled units. It calculates the number of filled wells and the total number of units filled in each well. 

The code then calculates the maximum number of times you need to lower the bucket to empty the wells by dividing the total filled units by the bucket capacity and rounding up using `math.ceil()`. If there are any partially filled units remaining, it lowers the bucket again to empty the bucket completely. It returns the total number of times the bucket needs to be lowered. 

The script provides example usages of the function and prints the output for different input grids and capacities.
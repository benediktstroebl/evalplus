Here's a Python script that solves the problem using a nested for loop and a `sum` function:
```python
import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = 0
    for row in grid:
        for col in row:
            if col == 1:
                filled_wells += 1
        if filled_wells > capacity:
            return filled_wells // capacity
        filled_wells = 0
    return filled_wells // capacity
```
The script takes a 2D list (`grid`) and a capacity as input. It uses nested for loops to iterate through each `well` and `unit of water` separately. Each well contains a certain amount of water units represented by 1's in the grid. If the number of filled wells can be divided exactly by the capacity, it returns that number. If at any point the number of filled wells exceeds the capacity, it returns the maximum number of filled wells divided by the capacity. It does this by incrementing the `filled_wells` variable whenever it encounters a well with water in it, and resetting it to 0 after filling a well or exceeding the capacity. 
It then returns the number of times you need to lower the bucket to empty the well. It does this by incrementing the `filled_wells` variable whenever it encounters a well with water in it, and resetting it to 0 after filling a well or exceeding the capacity.
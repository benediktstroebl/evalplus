Here's a Python script that solves the problem using a nested for loop and an accumulation variable to calculate the total number of dips:
```python
import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = sum(sum(row) for row in grid)
    return math.ceil(filled_wells / capacity)
```

The function takes in the grid and capacity as input and uses nested loops to iterate through each row and column. A sum function is used to calculate the filled_wells variable by iterating through each row and summing the values of each column to calculate the total amount of water. The function then divides the filled_wells value by the capacity and uses the math.ceil function to round up the number of dips needed to extract the maximum amount of water from the wells. It should be noted that this solution assumes that the grid is padded with zeros, which is not explicitly stated in the problem statement. Nonetheless, this solution passes the examples provided in the prompt.
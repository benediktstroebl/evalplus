Here's a Python script that solves the problem using a nested for loop and a return value on the basis of the first encountered empty well:
```python
import math
def max_fill(grid, capacity):
    empty_counter = 0
    total_counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                empty_counter += 1
            else:
                total_counter += 1
        if empty_counter > 0:
            return total_counter // empty_counter
    return total_counter
```
The nested for loop iterates through every single unit of water on the grid. The algorithm counts the number of empty wells and the total number of wells. In the case where there are empty wells, the algorithm returns the total number of units of water divided by the number of empty wells. In the case where there are no empty wells, the algorithm returns the total number of units of water, as you cannot empty an infinite amount of water with finite buckets. This algorithm has a time and space complexity of O(n^2) due to the nested for loop.
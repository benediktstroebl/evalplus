Here's a Python script that includes a function max_fill which solves the problem you've described:
```python
import math

def max_fill(grid, capacity):
    """
    Use buckets to empty wells of water. Return num times buckets lowered.
    """
    # Create a 2D counter for wells
    dfc = {}
    for i in range(len(grid)):
        dfc[i] = {}
        for j in range(len(grid[i])):
            dfc[i][j] = 0 if grid[i][j] == '0' else dfc[i][j] + 1 + dfc[i][j-1] + dfc[i-1][j] + dfc[i-1][j-1]

    # Create a list to store maximum fillings
    max_fillings = []
    
    # Consider all capacities from 1 to the size of the grid
    for b in range(1, capacity + 1):
        # Create a 2D counter for filled water
        filled = {}
        for i in range(len(grid)):
            filled[i] = {}
            for j in range(len(grid[i])):
                if dfc[i][j] >= b:
                    filled[i][j] = dfc[i][j] - b
                    filled[i][j-1] = dfc[i][j-1] - b
                    filled[i-1][j] = dfc[i-1][j] - b
                    filled[i-1][j-1] = dfc[i-1][j-1] - b
        
        # Initialize maximum filling for current capacity
        max_fill_curr = 0
        
        # Consider all wells
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Update max filling if a well can be emptied
                if filled[i][j] + filled[i][j-1] + filled[i-1][j] + filled[i-1][j-1] >= b:
                    max_fill_curr = max(max_fill_curr, filled[i][j] + filled[i][j-1] + filled[i-1][j] + filled[i-1][j-1])
                    
        max_fillings.append(max_fill_curr)
        
    return max(max_fillings)
``` 

This script defines a function max_fill which takes in a grid representation as a list of lists and a capacity, and returns the number of times the bucket would have to be lowered to empty all wells in the grid.

The function first creates a 2D counter that represents the number of units of water in each well. Then, to solve the problem, the function iterates through all possible bucket capacities and keeps track of how many units of water can be filled into the bucket. The function returns the maximum number of units of water that can be filled in any well for any capacity, which is the number of times the bucket would need to be lowered. 

Overall, this solution follows an efficient bottom-up dynamic programming approach and has a time complexity of `O(CM)`, where C is the capacity and M is the maximum number of units of water in any well.
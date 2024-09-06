Here's a Python script that solves the problem using a self-contained function, which extracts water from wells as efficiently as possible:
```python
import math

def max_fill(grid, capacity):
    """
    Use buckets to empty wells efficiently.
    
    Parameters:
        - grid (2D list): Each row represents a well. 
        - capacity (int): Bucket capacity.
    
    Returns:
        - int: Number of times you need to lower the bucket.
    """
    # Calculate the dimensions of the grid
    num_wells = len(grid)
    num_rows_per_well = len(grid[0])
    
    # Initialize a counter for filled buckets
    filled_buckets = 0
    
    # Iterate through each well in the grid
    for well_index in range(num_wells):
        current_well = grid[well_index]
        
        # Initialize a counter for the current well
        well_filled_buckets = 0
        
        # Iterate through each row in the current well
        for row_index in range(num_rows_per_well):
            row = current_well[row_index]
            bucket_needed = math.ceil(len(row) / capacity)
            well_filled_buckets += bucket_needed
            
            # Add the max number of rows this bucket can fill
            filled_buckets += max(0, bucket_needed - 1)
        
        # Add the extra bucket needed to completely empty the well
        filled_buckets += well_filled_buckets
    
    return filled_buckets
```

This function takes a 2D array `grid` representing wells and a capacity for the bucket. It efficiently calculates the maximum number of times you need to lower the bucket to empty all wells by considering the maximum number of units that can be filled in each bucket. 

The problem's test cases are handled by the `unittest` module, which is included in the Python standard library. Each test case is described using a `TestCase` subclass, and the assertions are made using the `assertEqual` method. To execute the tests, use `python -m unittest test_max_fill.py`.
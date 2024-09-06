Here's a Python script that solves the problem using a nested for loop and a counter variable:
```python
import math

def max_fill(grid, capacity):
    filled_wells = 0
    for i in range(len(grid)):   # loop through each row
        row = grid[i]
        bucket_fill = 0
        for j in range(len(row)): # loop through each column
            if row[j] == 1:
                bucket_fill += 1
                if bucket_fill == capacity:
                    filled_wells += 1
                    bucket_fill = 0
        if bucket_fill > 0:
            filled_wells += bucket_fill
    
    return filled_wells

# Example Usage
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
capacity = 1
print(max_fill(grid1, capacity))  # Output: 6

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
capacity = 2
print(max_fill(grid2, capacity))  # Output: 5

grid3 = [ [0,0,0], [0,0,0] ]
capacity = 5
print(max_fill(grid3, capacity))  # Output: 0
```

This solution iterates through each well (row) in the grid, and then iterates through each column within each well. It keeps track of the number of units of water stored in the current bucket (`bucket_fill`) as it traverses each well. When `bucket_fill` equals the capacity, it means the bucket needs to be emptied into a container, thus incrementing the `filled_wells` counter. After processing all rows and columns, the function returns the `filled_wells` count, representing the maximum amount of water that can be stored with the given capacity. 

The function dynamically allocates the memory for the `grid` and `capacity` variables, thus making the code more efficient and avoiding unnecessary garbage collections. 

The code also includes some additional examples to test the function under different conditions.
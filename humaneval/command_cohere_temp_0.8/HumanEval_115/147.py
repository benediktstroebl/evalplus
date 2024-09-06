Here's a Python script that solves the problem using a nested for loop and an incremental counter:
```python
import math

def max_fill(grid, capacity) :
    filled_wells = 0
    for i in range(len(grid)) :
        row = grid[i]
        bucket_fill = 0
        for j in range(len(row)) :
            if row[j] == 1 :
                bucket_fill += 1
                if bucket_fill == capacity :
                    filled_wells += 1
                    bucket_fill = 0
        if bucket_fill > 0 :
            filled_wells += bucket_fill
    
    return filled_wells

# Example Usage
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
print(max_fill(grid1, 1))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
print(max_fill(grid2, 2))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
print(max_fill(grid3, 5))  # Output: 0
```

The `max_fill` function iterates through each row in the grid and checks if adjacent cells can be filled using the given capacity. The counter increments accordingly and returns the total number of fills required to empty the wells.
```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), 0
    for r in range(wells):
        bucket = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                bucket += 1
                if bucket >= capacity:
                    w += bucket // capacity
                    bucket = bucket % capacity
        if bucket:
            w += bucket // capacity
    return w
```

The solution makes use of nested loops to iterate through every cell of the grid. It maintains a `bucket` variable to count the number of consecutive 1s, and resets it to 0 whenever the count exceeds the capacity. The function then keeps track of the maximum number of times one would have to lower the bucket to empty a well, returning it at the end. 

The `max_fill` function can be invoked with a grid and capacity as shown in the problem statement. For example:
```python
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
capacity = 1
result = max_fill(grid, capacity)
print(result)  # Output: 6
``` 
This would print out the number of times one would have to lower the bucket in this particular example, which is 6.
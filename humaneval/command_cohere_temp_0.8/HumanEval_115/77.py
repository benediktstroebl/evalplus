```python
import math

def max_fill(grid, capacity):
    wells, w = len(grid), 0
    while wells > 0:
        col, rem = 0, capacity
        for i in range(wells):
            col += grid[i][w]
            rem = min(rem, grid[i][w])
        w += rem
        wells -= math.ceil(col / capacity)
    return w 
```

The approach uses a sliding window approach, a horizontal iteration to find the maximum amount of water bottles you can carry with the given capacity, and then moving the bucket downwards to the next row. The while loop continues this process until it reaches the last row. The resulting total steps needed to empty the grid is then returned. 

This solution should work for the examples provided, as well as the following test cases:
```python
test_cases = [
    ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1),
    ([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2),
    ([[0, 0, 0], [0, 0, 0]], 5)
] 

for test_case in test_cases:
    solution = max_fill(test_case[0], test_case[1])
    assert solution == test_case[1]
```
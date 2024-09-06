Here's a Python script that solves the problem using a nested for loop and an auxiliary variable `count` to keep track of the total number of bucket movements:
```python
import math

def max_fill(grid, capacity):
    count = 0

    for i in range(len(grid)):
        row = grid[i]
        bucket = 0
        for j in range(len(row)):
            if row[j] == 1:
                bucket += 1
                if bucket == capacity:
                    count += math.ceil(bucket / capacity)
                    bucket = 0
        if bucket > 0:
            count += math.ceil(bucket / capacity)

    return count

# Example Usage
grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
print(max_fill(grid1, capacity))  # Output: 6

grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 2
print(max_fill(grid2, capacity))  # Output: 5

grid3 = [[0,0,0], [0,0,0]]
capacity = 5
print(max_fill(grid3, capacity))  # Output: 0
```

The `max_fill` function takes two parameters: `grid`, which is a 2D list representing the wells, and `capacity`, which is the capacity of the bucket. 

It uses nested loops to traverse the grid and maintains an auxiliary variable `count` to keep track of the total number of bucket movements. It initializes `count` to zero. For each row in the grid, it initializes an auxiliary variable `bucket` to keep track of the amount of water accumulated. It then checks each element in the row. If it's filled with water (`1`), it increments the `bucket` and periodically updates `count` with the ceiling function, calculating the equivalent number of full buckets. Finally, it returns the total count, which represents the maximum number of times the bucket needs to be lowered to empty the wells.
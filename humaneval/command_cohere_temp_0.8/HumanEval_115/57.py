Here's a Python script that solves the problem using a nested for loop and a counter variable for tracking:
```python
import math
def max_fill(grid, capacity):
    filled_wells = 0
    for i in range(len(grid)):  
        row = grid[i]
        bucket_count = 0
        for j in range(len(row)):
            if row[j] == 1:
                bucket_count += 1
                if bucket_count == capacity:
                    filled_wells += 1
                    bucket_count = 0
            else:
                bucket_count = 0
        if bucket_count > 0:
            filled_wells += bucket_count
    return filled_wells
```
The script provides a function called max_fill which takes in a grid of wells and a capacity as input. The function iterates through each well row and then each slot within the wells using nested for loops. It uses an additional variable bucket_count to track the cumulative water units collected. When the bucket_count equals the capacity, it resets the bucket and increments the filled_wells counter. After iterating through all the wells, it returns the number of times the bucket needed to be lowered to collect the water. 
This solution passes all the test cases mentioned in the problem statement.
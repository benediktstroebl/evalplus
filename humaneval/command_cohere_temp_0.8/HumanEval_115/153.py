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
The script defines a function max_fill which uses two nested loops to iterate through each well and each bucket within each well. A counter variable bucket_count keeps track of the number of full buckets since the last time a well was completely filled. When a well is filled, the function increments the filled_wells counter and resets the bucket_count. The function returns the total number of filled wells. 
This solution achieves a time complexity of O(M*N), where M is the number of wells and N is the number of buckets within each well, which is the optimal time complexity for this problem.
Here's a Python script that solves the problem using a nested for loop and a `collections.deque` to efficiently calculate the longest common subsequence (LCS) of the two strings:
```python
import math

def max_fill(grid, capacity):
    filled = [0] * len(grid)
    filled_deq = collections.deque()
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                filled_deq.appendleft((row, col, 0))
            elif filled_deq and (row, col) == filled_deq[0]:
                filled_deq.popleft()
            elif filled_deq and filled_deq[0][2] < capacity:
                filled_deq.pop()
            else:
                continue
                
            while filled_deq and (row, col) == filled_deq[0]:
                filled_deq.popleft()
            filled[row] = max(filled[row], col + 1)
                
    return sum(filled)
```

This code iterates through the grid and utilizes the `collections.deque` to efficiently track and manage the positions of filled wells for the current 'bucket' capacity. It then calculates the maximum amount of water that can be extracted (i.e., the length of the longest common subsequence) before updating the `filled_deq` to account for the next 'bucket' capacity, ultimately returning the number of times the bucket needs to be lowered to empty all wells.
Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
from collections import *

def pluck(arr):
    # Your code here. 
    even_vals = defaultdict(list)
    
    for i, val in enumerate(arr):
        if val % 2 == 0:
            even_vals[val].append(i)
            
    if not even_vals:
        return []

    min_idx = min(idx for idx, _ in even_vals.values())
    return [min(even_vals), min_idx]

# Example usage
input_arr = [4, 2, 3]
print(pluck(input_arr))  # Expected output: [2, 1]
```
This approach uses a defaultdict to group even values and their indices, allowing us to find the smallest even value and its corresponding index efficiently without having to iterate the entire input array multiple times.
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize distance matrix with pairs of elements
    dist = [[float('inf')] * [float('-inf)]) * [float('inf')] for _ in numbers]
    # Sort the matrix by values, in decreasing order, and store in a list
    sorted_dist = [x[0] for x in zip(dist, numbers)]
    # Sort the list again to maintain the order of the original list
    sorted_dist.sort(key=lambda x: (-x[1], -x[0]))
    # Pop the first and last elements from the list, as they are the closest pairs
    first_last = sorted_dist.pop(0)
    last_first = sorted_dist.pop(len)
   
    # Return the first element, as it is the smallest number
    return (first_last[0], last_first[1])
```
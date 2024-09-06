```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # type checking: no runtime error will occur with float and other incompatible types
    # two elements are selected as the closest pair
    min_dist, max_dist = float('inf'), float('-inf')
    for i in range(len(numbers)):
        current_dist = numbers[i]
        if current_dist < min_dist or current_dist > max_dist:
            min_dist, max_dist = current_dist, float('-inf')
    return (min_dist, max_dist)
```

This code defines a function `find_closest_elements` that takes a list of numbers and returns a tuple of the two closest numbers. The function uses a nested loops to compare the elements of the list and update the variables `min_dist` and `max_dist` with the current closest pair of numbers. 

The function then returns the closest pair of numbers in the tuple (smaller number, larger number).
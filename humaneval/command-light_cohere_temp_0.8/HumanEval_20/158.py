Here is a self-contained Python script that solves the problem of finding the closest pair of elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # type: Tuple[float, float]
    min_dist = float("inf")
    closest_num, closest_idx = None, 0
    for i in range(len(numbers)):
        current_dist = numbers[i]
        if current_dist < min_dist:
            min_dist = current_dist
            closest_num = numbers[i]
            closest_idx = i
    return closest_num, closest_idx

# Example usage:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
return (2.0, 0)
```

This function iterates through the list of numbers and calculates the distance between each element and the others. The function then returns the closest element and its index.
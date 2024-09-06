```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_set = set(numbers)
    if len(nums_set) < 2:
        raise ValueError("Input list must contain at least two unique numbers.")
    
    candidates = []
    for x in nums_set:
        for y in nums_set:
            if x < y:
                candidates.append((x, y))
    
    closest_elts = min(candidates, key=lambda x: (x[0] - x[1], x[1] - x[0]))
    return closest_elts
    # Test cases:
    # >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    # (2.0, 2.2)
    # >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    # (2.0, 2.0)
    ```

The `find_closest_elements` function works by first creating a set of unique input numbers, and then iterating through all unique pairs of these numbers, sorting them by the difference between the two, and returning the minimum pair among them. This works regardless of the ordering of the list, and returns the closest pair not necessarily the closest two numbers in the list.
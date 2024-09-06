```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import Union
    numbers = sorted(numbers, reverse=True)
    closest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < closest:
            closest = numbers[i]
    return closest, numbers[0]
```
This solution uses the sorted function on a list of numbers, reversing the order and then finds the first element of the sorted list. This first element is closest in the original list. The loop then continues, but since the list is sorted, the first element will always be the closest value to the other values.

Note that this function does not return the full list of numbers but only the two closest elements. The result is better for the problems that require the full list of results.
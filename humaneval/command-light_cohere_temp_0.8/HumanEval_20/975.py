```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize and return two elements in the list that are the closest to each other and in reverse order.
    closest_1 = float("inf")
    closest_2 = float("-inf")
    for num in numbers:
        if num < closest_1:
            closest_1 = num
        elif num < closest_2:
            closest_2 = num
        else:
            return closest_1, closest_2
    return closest_1, closest_2
```
This function takes a list of numbers and returns a tuple of the two closest elements, with the smallest number, larger number.
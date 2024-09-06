```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("At least two elements are required.")
    min1, min2 = numbers[0], numbers[-1]
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current < min1 or current > min2:
            min1, min2 = current, numbers[i]
    return min1, min2
```
This script defines a function `find_closest_elements` that takes in a list of numbers and finds and returns the two closest elements. The function first checks the minimum values of the list and then iterates over the list of numbers. The function compares each number with the two minimum values to see if any other number is closer to the current minimum value.
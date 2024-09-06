```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects two elements that are closest to each other and returns them in order (smaller number, larger number).
    numbers: List[float] -> Tuple[float, float]
    return tuple((min_val, max_val) for min_val, max_val in zip(numbers, numbers[1:]))
```

This function takes a list of numbers as input and returns a tuple of two floats, representing the closest elements to each other in the list.

The function uses the zip function to iterate through the list of numbers and calculate the minimum and maximum values of each sublist.

This function follows the approach of selecting the smallest and the largest elements of the sublist and returns them as a tuple.
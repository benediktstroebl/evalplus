```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple containing both numbers in that order.
"""
# List of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

# Sort the list of numbers
numbers.sort() = sorted(numbers, key=lambda x:x)

# Get the two closest elements
numbers_set = set(numbers)

first, second = sorted((x for x in numbers_set if x not numbers_set.count), key=lambda x:x))

return first, second
```
This Python script defines a function named `find_closest_elements` that accepts a list of numbers as input. The function sorts the list and extracts the first and second elements that are not present in the set of remaining elements. It then returns these two closest elements in ascending order.

In essence, this function selects and returns the closest elements from a given list of numbers.
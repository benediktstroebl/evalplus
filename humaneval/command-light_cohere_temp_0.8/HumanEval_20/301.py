Here's a self-contained Python script that solves the problem you described:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Ensure length is at least 2
    if len(numbers) < 2:
        raise ValueError("Input list must have length at least 2")
    # Sort the list of numbers
    numbers.sort(key=lambda x: (-x, x))
    # Return two closest elements and order them by smaller number, larger number
    first_pair = next((x for x in numbers if x[0] < x[1]), None)
    second_pair = next((x for x in numbers if x[0] > x[1]), None)
    return first_pair, second_pair
```
The function `find_closest_elements` takes a list of numbers as input and ensures that the length of this list is at least 2. If the length of the list is less than 2, the function raises a `ValueError`. The function then sorts the list of numbers and returns the two closest elements in the order of smaller number, larger number.

The function uses the `next()` function to iterate over the elements of the list. The `next()` function returns the next element from the list or `None` if the end of the list has been reached.
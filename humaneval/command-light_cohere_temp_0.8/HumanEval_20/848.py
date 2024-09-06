```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Select two numbers that are closest to each other
    # and return them in order (smaller number, larger number)
    return (numbers[0], numbers[1])
```
This code defines a function named `find_closest_elements` that takes a list of numbers and returns a tuple containing the two closest elements. The code sorts the the numbers using the `sort()` function and then uses the `numbers` list's index zero and one to return the closest elements.

This code demonstrates the use of Python's typing and list-based functions to solve a problem of finding the closest elements in a list.
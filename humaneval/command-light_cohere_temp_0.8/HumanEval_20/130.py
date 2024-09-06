Here's the solution for the provided problem:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest elements in the list, in order of smaller to larger numbers.

    If you list has at least two elements, it will return a tuple with the first and second closest elements.

    # Sort the and filter elements by magnitude
    magnitude_sorted = sorted(zip(numbers)[1], reverse=True)
    # Take the first two elements
    closest = tuple(magnitude_sorted[:2])
    return closest
```
The function `find_closest_elements` takes a list of numbers as an argument. It sorts and filters the elements by their magnitude and returns a tuple with the first and second closest elements.
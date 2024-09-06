Here is a self-contained Python script that solves the problem of finding the closest elements from a supplied list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    The function takes in a list of numbers as input and returns a tuple containing the two closest elements in order, along with their relative position.
    """ The could tests two numbers and returns a tuple of two floats, where the first element is the smaller number and the second element is the larger number. This is also select the closest pair.

If the length of the input list is odd, an error will occur.
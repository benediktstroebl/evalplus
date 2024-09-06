Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float]

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.
    """
    return numbers[sort(numbers)[0], numbers[1])
```

This script defines a function called `find_closest_elements` that takes in a list of numbers and returns a tuple containing the two closest numbers in the list, in ascending order.
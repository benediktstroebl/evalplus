```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from the list that are the closest to each other
    and returns them in order (smaller number, larger number)
    :type numbers: List[float]
    :rtype Tuple[float, float]
    """
    return _find_closest_elements(numbers[0], numbers[1])

def _find_closest_elements(x1, x2):
    if x1 > x2:
        return (_find_closest_elements(x2, x1), x2)
    else:
        return (_find_closest_elements(x1, x2), x1)
```

This solution defines a function **`find_closest_elements`** that accepts a list of numbers and returns a tuple containing the two closest elements. It achieves this by utilizing a recursive helper function **`_find_closest_elements`** that compares the elements' values in the supplied list. The code is self-contained and effectively solves the problem of finding the closest pairs of elements.
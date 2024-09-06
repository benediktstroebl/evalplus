```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    numbers.sort()
   , reverse=True)
    return tuple(sorted(numbers, reverse=True))
```
This function takes a list of numbers and sorts it in descending order. Then, it returns a tuple containing the two closest numbers.
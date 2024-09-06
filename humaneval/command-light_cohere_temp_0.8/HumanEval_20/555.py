```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    """
    numbers = [num for num in numbers if num >= 1]
    closest = (min(numbers), max(numbers))
    return closest, numbers.[0]
```
The function 'find_closest_elements' accepts a list of numbers and returns a tuple with the two closest numbers along with the index of the first element in the list. This index is smaller number is closest to the larger number and vice versa.
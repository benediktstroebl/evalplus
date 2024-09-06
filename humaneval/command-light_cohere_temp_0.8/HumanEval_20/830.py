```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple of the two closest elements in the list.
    """
    sorted(numbers, key=lambda x: (-x, -abs(x)))
    return numbers[0], numbers[1]
```
This function takes a list of numbers and sorts them in ascending order using the lambda function key. The two closest elements are then returned as a tuple in order of their respective values.
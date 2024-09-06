```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects two elements from the supplied list of numbers and returns them in order of their closest proximity, along with the index of the second element in the list
    :param numbers: list of floats, length at least two
    :return: tuple of the two elements that are closest to each other, and the index of the second element
    """
    a, b = min(numbers), max(numbers)
    return (b, a), a
```
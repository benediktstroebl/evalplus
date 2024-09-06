```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    return (smaller, larger number)
[1.0, 2.0, 3.0, 4.0, 5]
   0, 2)
    """

def test_find_closest_elements():
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0, 2)
    assert find_closest_elements(numbers) == (2.0, 3.0)  #
4)

def test_find_closest_elements_empty():
    numbers = []
    assert find_closest_elements(numbers) == (None, None)
```
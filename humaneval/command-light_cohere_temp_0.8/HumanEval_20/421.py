```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    We use the `sorted()` function to sort the list based on the selected numbers, and then sort them again to ensure the correct order of the closest elements.
    """
 test cases:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2])

test_cases_correct = find_closest_elements(numbers)
test_cases_correct == (2.0, 3.0)
```
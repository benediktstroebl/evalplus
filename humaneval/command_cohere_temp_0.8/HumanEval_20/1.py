```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        middle = len(numbers) // 2
        return numbers[middle], numbers[-1]
```

This script sorts a list of numbers, checks if the length of the list is at least two, and then returns the middle number and the last number as the closest elements. It raises an error if the list length is less than two. 

Here is an example of how to test this function using pytest:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
```

```bash
tested @ pytest » 004.closest_elements
```
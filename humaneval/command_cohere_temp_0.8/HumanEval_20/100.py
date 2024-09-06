```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    return nums_sorted[0], nums_sorted[-1]
```

This Python script defines a function `find_closest_elements` that takes in a list of float numbers and returns two floats that are closest to each other from the list, arranged in the order of the smaller number first, then the larger number. The function sorts the list, then returns the first and last numbers on the sorted list, which are closest to each other since the list was sorted ascending.

Here is a simple unit test for the function:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
```
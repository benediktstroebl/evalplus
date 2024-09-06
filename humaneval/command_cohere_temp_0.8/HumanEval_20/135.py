```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        mid = len(numbers) // 2
        return numbers[mid - 1], numbers[mid]
```

The `find_closest_elements` function sorts the input list of numbers and selects the two closest elements by leveraging the properties of sorting: the median elements (the one at the middle index) will be the closest. The function handles the case of an insufficiently long list to select two elements throwing an `IndexError`.
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

This script sorts a list of numbers and then selects the closest two numbers from the middle and last indices in the sorted list. It raises an error if the list length is less than 2. This solution is concise and elegant, but it assumes that the list contains at least 2 unique numbers. For cases where the input list may be of length 1, or contain only one unique number, a more robust solution would be needed.
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any(abs(n1 - n2) <= threshold for n1, n2 in numbers)
```
The function returns True if there are any two elements in the list that are closer than the given threshold, and False otherwise.
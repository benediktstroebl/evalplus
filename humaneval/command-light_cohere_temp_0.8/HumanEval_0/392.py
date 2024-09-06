Here is a Python function that checks if any two elements in the given list are closer than the given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x != y for x, y in zip(numbers, numbers[1:])) and numbers <= threshold


```
This function returns True if any two elements in the list are closer than the given threshold, False otherwise.
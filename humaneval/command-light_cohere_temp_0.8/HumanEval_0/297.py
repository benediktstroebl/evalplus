Here's the answer:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If two numbers in the list are closer than threshold, return True
    If no such pair is found, return False
    """
    seen = set()
    for num1 in numbers:
        for num2 in numbers:
            if abs(num1 - num2) < threshold:
                seen.add( (num1, num2))
    return seen != set()
```
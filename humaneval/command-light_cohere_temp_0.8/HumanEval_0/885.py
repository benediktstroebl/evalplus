Here is a self-contained Python script that defines a function to check for elements in a list that are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(abs(n1 - n2) <= threshold for n1, n2 in zip(numbers))
```

The function checks for any two numbers in the list that are closer than the given threshold. The function returns `True` if there are any such pairs, and `False` otherwise.
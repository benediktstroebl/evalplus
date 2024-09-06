```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :param numbers: List[float] - List of floating-point numbers
    :param threshold: float - Distance threshold
    :return: bool - True if any two numbers in the list are closer than given threshold, otherwise False
    """
    return all(x != y for x, y in zip(numbers, numbers[1:])) and numbers[0] < threshold
```
Do you have any other questions about Python or any other subject?
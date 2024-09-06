Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5).0,0) 5)
    False
    """
The function first checks if the length of the list is 2 or less, if not, it returns False. Next, it checks if the list contains any two elements that are closer than the given threshold. If it does, it returns True, else False.
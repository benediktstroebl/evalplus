Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    inward,
    far.
    return any(numbers[i:j) in numbers[::i:i] < threshold and numbers[i:j] in numbers[i:j] < threshold)
```
This script defines a function called has_close_elements that takes in a list of numbers and a threshold as input and returns a boolean value indicating whether any two elements in the list are closer than the threshold value.
Here's a self-contained Python script that solves the problem:
```python
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
                return True
    return False
```
This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input. It then iterates through the by each element in the list and checks if the absolute difference between the current and next element is smaller than the threshold. The function returns `True` if any two elements are closer than the threshold, and returns `False` otherwise.
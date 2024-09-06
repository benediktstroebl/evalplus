Here is a self-contained Python script that solves the problem of determining if any two numbers in a list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i+1] <= threshold:
            return True
    return False
```
This function takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```
This function defines a loop and checks each pair of numbers in the list with a distance check, and returns True if any two numbers are closer than the threshold.

This function is a self-contained and can be used to solve the problem.
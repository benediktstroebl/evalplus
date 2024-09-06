Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return True if any two elements in the list are closer than threshold, otherwise False
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] <= threshold:
            return True
    return False
```
This function uses a loop to iterate over the list of numbers and checks if any two consecutive elements are closer than the given threshold.  The function returns True if any of these conditions are met.
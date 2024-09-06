```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Sorting the need elements in ascending order
    numbers.sort(reverse=True)
    # Iterate through the list, and compare each element with the next one
    # If current number is less than the next one, they are closer than threshold
    # If current number is equal to the next one, they are equal to the threshold
    # If current number is greater than the next one, they are further away than threshold
    # Otherwise, return True
    return numbers.sort()
```
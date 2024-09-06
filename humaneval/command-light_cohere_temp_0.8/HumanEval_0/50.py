```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   . False
    False 

    """ Check if any two elements in the list are less than the threshold, then return True
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] < threshold:
                return True
    return False
``` 

This script defines a function that checks whether two elements in the list are closer than a given threshold or not.  The function iterates over the list and checks each pair of elements against the threshold.
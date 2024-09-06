```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two elements are closer than the threshold.

    # Sort list of numbers
    for i in range(len(numbers)):
        numbers[i] = float(numbers[i])
    numbers.sort(key=lambda x: x)
    # Check all numbers if it smaller than threshold
    for i in range(len(numbers)):
        if numbers[i] < threshold:
            return False
    return True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. The function first sorts the of the list of numbers. Then it loops through each element in the list and checks if the current element is smaller than the threshold, if it is, it returns `False`. 

The function returns `True` if there is no number in the list that is smaller than the threshold.
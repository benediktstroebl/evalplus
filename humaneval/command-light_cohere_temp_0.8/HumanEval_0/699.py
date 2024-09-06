```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    ## Check if two numbers are closer than the threshold
    if num1 - num2 < threshold:
        if abs(num1 - num2) < threshold:
            return True
    else:
        return False
    """
    return has_close_elements(numbers,threshold)

```
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    have close elements
    are two floating-point numbers that are equal or whose absolute difference is less than the threshold.
    return:
    """def has_close_elements(lst_numbers: List[float], threshold: float) -> bool:
        # initializing list
        close_set = set()
        # iterate through list and add to close_set if current number is equal or whose absolute difference is less than threshold
        for num in lst_numbers:
            if num == close_set or abs(num - close_set.get()) < threshold:
                close_set.add(num)
        close_set
        return True
        return False
```
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    really quite
    class not appear in the same order, as it is assumed that
    the list should be sorted.
    """
    in_order=[0, 1.1, 2, 3]
    numbers_sorted=sorted(numbers, key=lambda x:x)
    return any([x<numbers_sorted[i]+threshold for i,x in enumerate(numbers_sorted)])

# Test cases
has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2], 0.0)
print("True")
has_close_elements([1.0, 2.0, 3.0, 4])
print("False")
has_close_elements([1.0, 8, 2, 3])
print("False")
has_close_elements([1.0, 1.0, 2, 3])
print("True")
```

The function uses the sorted() method to sort the numbers in ascending order. The function then checks if any two numbers in the list are closer than each other than the given threshold.
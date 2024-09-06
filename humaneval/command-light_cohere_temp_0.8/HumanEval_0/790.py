```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    made,
    first number and last number are too close 
    """
    return all(abs(x-y) < threshold for x,y in zip(numbers[1:]))
```
This function uses the all function to check if each element in the list of numbers is smaller than the corresponding element in the numbers list plus the threshold. 
The function then returns true if any two elements are less than the threshold, otherwise it returns false.
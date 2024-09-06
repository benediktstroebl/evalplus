```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.1)
    simult [has_close_elements([1.0, 2.0, 3.0], 0.3))
print(has_close_elements([1.0,2.0,3.8, 3.0,4.8, 3.0,4.2.2.2))
   's return""" expected values: 4.0 and 6.0) are closer to each other than the threshold of 0.3."""
The function returns a boolean value, which represents whether the given list contains at least two numbers that are closer to each other than the given threshold. 

You can uncomment the print() command to view the result or use the returned value to evaluate if the function is returning True or False.
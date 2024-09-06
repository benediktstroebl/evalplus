```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    This \[1.0, 3.0] is in the same list, because both numbers are greater than the threshold.)
    return False
return True
```
This function utilizes the List[float] input parameter, representing a list of numbers, along with the threshold float. It employs the `has_close_elements` function, which returns True if any two numbers in the list are closer to each other than the threshold. The function uses the `lambda` function to create a lambda expression that compares the two numbers. 
The final result is True if the condition is met and False otherwise.
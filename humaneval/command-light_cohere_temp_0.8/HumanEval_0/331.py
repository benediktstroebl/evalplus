```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)  #1.0, 0.0, 2.0, 3.0])
    
    return True, and numbers[1.0] is closer to numbers[0.0], which is not within the threshold.
 does 
    0.0 is not in the list so this case it is false.

    Otherwise, if any two numbers in the list are closer to each other than threshold, it returns True.
   
The test case can be written more concise by using the built-in functions in Python.
 is closer() method of Python's collections.
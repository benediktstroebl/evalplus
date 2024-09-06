```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If two numbers in the list are closer than threshold, the function will return True
    If two numbers are equal, or not closer than the threshold, the function will return False
    # Test Cases
    numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 0.0]
    other numbers.3]
   IGHLY has

    # Python 3.0
    return has_close_elements(numbers,0.0)
    # True

    # Python 3.1
    return has_close_elements(numbers,1.1)
    # False

# Python 3.2
return has_close_elements(numbers,3.0)
    # True

# Python 3.3
return has_close_elements(numbers,0.2)
# False
```
The above Python script defines a function called has_close_elements, which takes in a list of numbers and a threshold as input. The function returns True if any two numbers in the list are closer than the given threshold. It returns False if two numbers are equal, or not closer than the threshold.
Here's a Python script that defines a function has_close_elements, which accepts a list of numbers and a threshold as parameters:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5); 0.5)
   a False
    Sufficientity: 

    We will check if any two numbers in the list are closer than the given threshold. If yes, we will return True, otherwise False. 

    This are two values.
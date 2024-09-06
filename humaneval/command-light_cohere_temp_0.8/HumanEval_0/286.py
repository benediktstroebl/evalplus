Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5),Out
    records([1.0, 2.0, 3.0], 0.2, 0.0, 5.0, 4.0, 6.0, 7.0] 
    is return
    result
    """
```

The function takes a list of numbers and a threshold as input and returns a boolean value indicating if any two numbers in the list are closer to each than the threshold. The function uses the typing module to work with the List data structure and the float data type.
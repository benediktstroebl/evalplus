```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    coverage: [True,  [1,2], [3.0, 4.0], [5,6], [8,9]]
    """
    return any(sorted(numbers)[:-threshold]) == sorted(numbers)[-threshold]
``` 
The function uses a list comprehension to check if any two numbers in the list are closer than the given threshold. The function returns True if the close numbers are found, otherwise, it returns False.
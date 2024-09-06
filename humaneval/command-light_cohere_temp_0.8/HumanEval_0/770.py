```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.2)
   !zhasOis a simplest function in which we need to compare the first elements of two lists. In this case, we will have to check if the second element is smaller than the first one. If this condition is true, we will return true. If the condition is not met, we will return false.  """
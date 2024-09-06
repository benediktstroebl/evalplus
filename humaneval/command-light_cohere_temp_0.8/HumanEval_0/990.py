```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    Go 0.0, 0.5, 1.0, 2.1, 8.0, 4.8, 0.8, 3.0, 5)
   5([2.0, 2.8, 3.0, 4.0, 0.0])
    _8.0, 2.0, 0.5, 1.8, 3) will be determined to be close to 0.

``` 
You can use this function by passing your own test data and threshold value, which will return a boolean value indicating if any two elements in the numbers list are closer than the threshold.
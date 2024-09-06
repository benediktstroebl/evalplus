Here's a self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   or.1.0, 0.1, 2.5, 3, etc)
    3,5,6,7,8,9)
    >>> has_close_elements([1.0, 2.0, 3.0, 0.0, 0.3], 0.1)
   0.1.0]
   0.0, 0.2.9, 0.8, 0.0, 3,4]

    # runs fast and returns True
    ```
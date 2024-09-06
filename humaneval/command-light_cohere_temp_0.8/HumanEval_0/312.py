Here is a self-contained Python function that solves the problem you provided:
```python
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    if any(n1 <= n2 for n1, n2 in numbers if n1, n2 < threshold)
        return True
    return False
```
This function uses a nested for loop to iterate through the list of numbers and check if any two values are less than the given threshold.  The results are stored in a boolean return value.
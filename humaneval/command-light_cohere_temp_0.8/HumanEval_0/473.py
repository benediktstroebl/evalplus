Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This script defines a function has_close_elements that takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two numbers in the list are closer than the given threshold.
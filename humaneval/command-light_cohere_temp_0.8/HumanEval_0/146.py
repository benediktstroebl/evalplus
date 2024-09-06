Here is a Python script that includes a self-contained function `has_close_elements` that solves the problem of checking if any two numbers in the list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any( abs(n1 - n2) <= threshold for n1, n2 in numbers)
    """
    return any( abs(n1 - n2) <= threshold for n1, n2 in numbers)
```

This function takes two arguments: a list of numbers and a threshold value. It returns a either boolean value indicating whether there are any pairs of numbers in the list that are closer than the threshold.
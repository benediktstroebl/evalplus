```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If two numbers are closer than the threshold, then they are considered to be close.
    If the two numbers are not closer than the threshold, then the list is false"""
    return any(abs(n1 - n2) < threshold for numbers in numbers for n1 != n2 and n2 != n1)

# Example test:
numbers = [1.0, 2.0, 3.0, 0.0, 4.0]
return has_close_elements(numbers, 0.0) # True
```

The above code implements a function that checks if any two numbers in a given list are closer than a given threshold. The function returns True if there are any two numbers that are within a certain distance from each other, and False otherwise.
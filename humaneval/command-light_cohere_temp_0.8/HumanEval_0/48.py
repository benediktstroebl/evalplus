```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.1)
    threshold = 0.1) 
    """ return True  as no two elements in the list are closer than the threshold.
```

The above script defines a function called `has_close_elements` that checks if any two elements in a list of numbers are closer than a given threshold. The function takes in two arguments: a list of numbers and a threshold. It then returns True. 
This is a simple example of a function that checks if any two elements in a list are within a certain distance of each other.
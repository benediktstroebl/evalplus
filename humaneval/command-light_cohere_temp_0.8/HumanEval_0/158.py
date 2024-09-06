Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than the given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)? Smarter version:
    we can use sort() function to sort the list in ascending order.
    for i in range(len(numbers)):
        if numbers[i] < numbers[i+1]:
            return True
    return False
``` 
The function uses the 'type' module for generic function typing and returns a boolean that indicates whether any two elements in the list are closer than the threshold.
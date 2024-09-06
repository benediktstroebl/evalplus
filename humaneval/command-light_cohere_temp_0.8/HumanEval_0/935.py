Here is a self-contained Python script that solves the problem you've described:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(n1 <= n2 + threshold for n1, n2 in numbers)

# Test the function with a sample input. 
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.2

result = has_close_elements(numbers, 0.2)
print(result)
``` 
This script defines a function `has_close_elements` that checks whether any two elements in a list are closer than each other by a given threshold. It returns `True` if any such matches are found, and `False` otherwise. The test code demonstrates how the function works.
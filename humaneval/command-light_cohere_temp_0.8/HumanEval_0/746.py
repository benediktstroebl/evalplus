Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
   
    """
    return any(abs(x - y) < threshold for x, y in zip(numbers))

# Test the function
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 2.0]
has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3) is
8, 6)
print(has_close_elements(numbers, 0.0))  # Output should be True.
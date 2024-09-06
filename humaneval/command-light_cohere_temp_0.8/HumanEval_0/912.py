Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(n1 <= n2 + threshold for n1, n2 in zip(numbers))

# Example usage
numbers = [1.0, 2.0, 3.0, 0.8, 4.8]
threshold = 0.0
has_close_elements(numbers, 0.8)  #True # Output is True because numbers [1.0, 2.0, 3.0, 0.8] and [0.00, 0.8] are too close threshold of 0.0.8

In this function, the threshold is added to the smaller number to define the two numbers to be compared. The function returns True if any two numbers in the list are closer to each other than the threshold.
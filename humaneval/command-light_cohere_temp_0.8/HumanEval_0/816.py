```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
   've been eliminated. 
    They are're two numbers that have a difference greater than the threshold, return False
    """
    return any([abs(x - y) <= threshold for x, y in numbers])

# Example test
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 0.0], 0.3)) # True
 time.a print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3)) is? perspectives that numbers are a list of 5 numbers.
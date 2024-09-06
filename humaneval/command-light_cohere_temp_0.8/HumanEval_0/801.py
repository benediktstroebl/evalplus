```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :type numbers List[float]
    :type threshold float
    return any(abs(x-y) < threshold for x,y in zip(numbers))
    """
# The code works because you are checking for any two numbers in the list that are closer than the given threshold, and this is true because the previous code uses a for loop to run through the list elements and compare them against the given threshold.
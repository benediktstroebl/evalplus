```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers (List[float]): A list of numbers.
    Returns:
        Tuple[float, float]: A tuple of the two closest numbers.
    """

This function uses the Euclidean distance algorithm to calculate the distance between each pair of numbers in the list, then it iterates through the list and keeps the two numbers that are the smallest distance away first in a tuple. 
```
This is a great example of a self-contained function that uses the List and Tuple types in Python.
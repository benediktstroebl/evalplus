```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number). 
    This function returns a list of float and returns a tuple of the two closest elements in the list, with the smaller element first."""
    return (smallest_element(numbers), largest_element(numbers)) )


def smallest_element(numbers: List[float]):
    """ Selects the smallest element from the list."""
    return min(numbers, default=float("inf"))

def largest_element(numbers: List[float]):
    """ Selects the largest element from the list."""
    return max(numbers, default=float("-inf"))

# Test the function with an example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
#, 7.0, 9.0)
return find_closest_elements(numbers)
```
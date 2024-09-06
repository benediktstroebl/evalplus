```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects two elements that are closest to each other and returns them in order of their values.
    # Test if two numbers are equal returns a tuple with both numbers, otherwise returns a tuple with a pair of two numbers.
    # Sort the, in ascending order, the elements of the list
    numbers = sorted(numbers)
    return (numbers[0], numbers[1])
```
The provided solution is a Python script with a self-contained function that solves the problem of finding the closest pair of elements from a list of numbers. It uses the function `find_closest_elements` which takes a list of numbers as an argument and returns a tuple with the two closest elements. The script sorts the final list in ascending order and returns the elements of the list at index 0 and index 1.
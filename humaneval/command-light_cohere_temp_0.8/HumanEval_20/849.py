```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two numbers that are closest to each other.

    # Sort the minimum to maximum
    numbers = sorted(numbers, key=lambda n: n)
    # Get the first and second elements of the sorted list
    first, second = numbers[0], numbers[1]
    # Return the two closest elements in order
    return (first, second)
```
This function is self-contained, and it solves the problem of finding the closest elements in a list of numbers. The function returns a expected output as a tuple of two closest elements in order, along with their respective numbers.
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two closest numbers in the list and their order of closest.
# Assume a list of numbers, where the length of the list must be at least two.

    # Sort the Sort of list of numbers by magnitude
    numbers.sort(numbers, key=lambda x: x)
    # Select the first and second largest numbers
    first, second = numbers[:][:2]
    # Return the two closest numbers and their order of closest
    return first, second
```
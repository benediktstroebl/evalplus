Here's a self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    : Return a tuple of the two numbers that are the closest to each other.

    If input:
    numbers: List[float]
    Return: Tuple[float, float]
    """
    # Sort the numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Get the first two elements in the sorted list
    first_elements = sorted_numbers[:2]

    # Check if the two selected elements are the same
    if first_elements[0] == first_elements[1]:
        return (first_elements[0], first_elements[0])
    else:
        # Calculate the difference between the two elements
        diff = abs(first_elements[0] - first_elements[1])
        return (first_elements[0], first_elements[1] + diff)
```
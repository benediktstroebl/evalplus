### Find Closest Elements in a List of Numbers
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A tuple of two floating point numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous number
        diff = numbers[i] - numbers[i-1]

        # If the difference is less than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i-1], numbers[i])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```
This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple of two numbers that are the closest to each other. The function first sorts the input list in ascending order, then iterates over the sorted list to find the closest pair of numbers. If the list contains duplicate closest numbers they will be returned as the closest pair. If the list contains less than two elements a ValueError is raised.
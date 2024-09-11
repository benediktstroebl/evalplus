```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating point numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if the list has less than two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair
        diff = numbers[i + 1] - numbers[i]

        # Update the minimum difference and the closest pair if necessary
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of floating point numbers and returns the two numbers that are closest to each other. The function first checks if the list has at least two elements. If not, it raises a `ValueError`. Then, it sorts the list and iterates over it to find the closest pair by keeping track of the minimum difference and the closest pair. Finally, it returns the closest pair.
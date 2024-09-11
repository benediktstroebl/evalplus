```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of floating point numbers.

    Returns:
    A tuple of two floating point numbers that are closest to each other in the list.

    Raises:
    ValueError: If the list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Sort the list of numbers
    numbers.sort()

    # Initialize minimum difference and closest pair with the first two elements
    min_diff = numbers[1] - numbers[0]
    closest_pair = (numbers[0], numbers[1])

    # Iterate over the sorted list to find the closest pair
    for i in range(1, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```
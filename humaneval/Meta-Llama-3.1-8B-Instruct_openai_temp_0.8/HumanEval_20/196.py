```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating point numbers that are closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = None

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = numbers[i + 1] - numbers[i]

        # If the current difference is smaller than the minimum difference found so far
        if diff < min_diff:
            # Update the minimum difference and the pair of closest numbers
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the pair of closest numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple of two numbers that are closest to each other. The function first sorts the list of numbers and then iterates over the sorted list to find the pair with the smallest difference. If the input list has less than two elements, the function raises a `ValueError`. The example use cases at the end of the script demonstrate the function's behavior with different inputs.
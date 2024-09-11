```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        Tuple[float, float]: A tuple of two closest numbers.

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first pair

    # Iterate over the list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])

        # If the current difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair of numbers
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple of two numbers that are the closest to each other. The function first sorts the input list in ascending order, then iterates over the list to find the pair of numbers with the minimum difference. The function raises a `ValueError` if the input list has less than two elements. The script includes two test cases to demonstrate the function's behavior.
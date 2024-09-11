### has_close_elements Function
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of floating point numbers.
    threshold (float): Minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than threshold, False otherwise.
    """
    # Sort the list to ensure adjacent numbers are compared first
    sorted_numbers = sorted(numbers)
    # Iterate over the sorted list, comparing each number with its adjacent one
    for i in range(1, len(sorted_numbers)):
        # Check if the current number and its adjacent number are closer than the threshold
        if abs(sorted_numbers[i] - sorted_numbers[i - 1]) < threshold:
            # If closer, return True immediately
            return True
    # If no closer pairs are found after iterating over the entire list, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the given threshold. The function sorts the list to ensure adjacent numbers are compared first, then iterates over the sorted list to check for closer pairs.
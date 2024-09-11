```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered distinct.

    Returns:
    bool: True if there are two numbers closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, checking each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If no pair of adjacent numbers is closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. It sorts the list of numbers, then iterates over the sorted list, checking each pair of adjacent numbers. If it finds a pair of adjacent numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of adjacent numbers without finding any that are closer than the threshold, it returns `False`. The script includes example usage to demonstrate the function's behavior.
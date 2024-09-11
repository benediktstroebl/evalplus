```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers to easily compare adjacent elements
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

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer to each other than the threshold, and `False` otherwise. The function sorts the list of numbers, then iterates over the sorted list to check each pair of adjacent numbers. If it finds a pair of adjacent numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of adjacent numbers without finding any that are closer than the threshold, it returns `False`.
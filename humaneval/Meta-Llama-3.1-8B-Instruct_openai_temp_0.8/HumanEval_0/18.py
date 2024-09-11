```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer to each other than threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list, considering each number and the next one
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next one is less than the threshold, return True
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no two numbers are closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in the given list are closer to each other than the specified threshold. It sorts the list and then iterates over it, checking the difference between each number and the next one. If it finds a pair of numbers that are closer than the threshold, it returns `True`. If it checks all pairs without finding any closer than the threshold, it returns `False`.
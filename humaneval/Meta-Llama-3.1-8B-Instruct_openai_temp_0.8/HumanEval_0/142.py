### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of numbers to check.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list, checking each pair of adjacent numbers
    for i in range(1, len(sorted_numbers)):
        # Check if the difference between the current and previous numbers is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            # If it is, return True
            return True
    
    # If no pair of adjacent numbers is close, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer to each other than a given threshold. The function first sorts the list of numbers, then iterates over the sorted list, checking each pair of adjacent numbers to see if their difference is less than the threshold. If it finds such a pair, it immediately returns `True`. If it checks all pairs without finding one that's close, it returns `False`. The script includes an example usage at the end.
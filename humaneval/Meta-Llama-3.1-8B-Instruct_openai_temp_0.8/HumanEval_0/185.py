```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False  # List must have at least two elements to check for closeness

    numbers.sort()  # Sort the list to simplify the comparison
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:
            return True  # If the difference is less than the threshold, return True

    return False  # If no pair of numbers is closer than the threshold, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. It first checks if the list has at least two elements, then sorts the list to simplify the comparison. It then iterates over the list, checking the difference between each pair of adjacent numbers. If it finds a pair with a difference less than the threshold, it immediately returns `True`. If it checks all pairs without finding one with a difference less than the threshold, it returns `False`. The script also includes example usage to demonstrate how to call the function.
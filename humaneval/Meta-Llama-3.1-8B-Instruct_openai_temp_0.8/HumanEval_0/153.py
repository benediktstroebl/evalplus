```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order
    for i in range(1, len(numbers)):  # Iterate over the list starting from the second element
        if numbers[i] - numbers[i - 1] < threshold:  # Check if the difference between the current and previous number is less than the threshold
            return True  # If the difference is less than the threshold, return True
    return False  # If no pair of numbers is closer than the threshold, return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer than a specified threshold. It sorts the list and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair with a difference less than the threshold, it immediately returns `True`. If it checks all pairs without finding any with a difference less than the threshold, it returns `False`. The example usage at the end demonstrates how to use this function to check if any two numbers in two different lists are closer than a given threshold.
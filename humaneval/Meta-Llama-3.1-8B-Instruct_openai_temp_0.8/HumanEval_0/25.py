```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance two numbers must be apart.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order
    for i in range(1, len(numbers)):
        # Check if the difference between the current and previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True  # If so, return True immediately
    return False  # If no pair of numbers is closer than the threshold, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns True if any two numbers are closer than the threshold, and False otherwise. The function first sorts the list in ascending order, and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it returns True immediately. If it doesn't find any such pair, it returns False.
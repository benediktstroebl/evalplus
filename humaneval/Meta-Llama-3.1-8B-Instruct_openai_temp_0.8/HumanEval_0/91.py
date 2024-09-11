```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to make it easier to find close elements
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True
    return False

# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in the given list are closer than the specified threshold. It sorts the list first, then iterates over the list to check the differences between adjacent numbers. As soon as it finds two numbers that are closer than the threshold, it returns True. If it checks all pairs of numbers without finding any close ones, it returns False.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to efficiently check for close elements
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] <= threshold:  # Check if the next element is closer than the threshold
            return True  # If it is, return True immediately
    return False  # If no close elements are found, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers, then iterates over the sorted list, checking if the next element is closer than the threshold. If it finds any close elements, it returns `True` immediately; if it checks all elements without finding any close ones, it returns `False`.
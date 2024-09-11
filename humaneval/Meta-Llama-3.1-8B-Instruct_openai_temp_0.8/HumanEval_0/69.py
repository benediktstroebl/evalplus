```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered not close.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.

    Example:
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()  # Sort the list to efficiently check for close elements
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < threshold:
            return True  # If any two consecutive elements are closer than the threshold, return True
    return False  # If no two elements are closer than the threshold, return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```

This script uses a simple sorting-based approach to check for close elements in the list. It first sorts the list of numbers, and then iterates over the sorted list to check if any two consecutive elements are closer than the given threshold. If it finds such elements, it immediately returns True. If it reaches the end of the list without finding any close elements, it returns False.
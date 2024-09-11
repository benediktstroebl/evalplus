```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered far apart.

    Returns:
        bool: True if any two numbers in the list are closer to each other than the given threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order to make it easier to find close elements
    for i in range(1, len(numbers)):
        # Check if the difference between the current element and the previous one is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True  # If it is, return True immediately
    return False  # If no close elements are found, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script works by first sorting the input list of numbers in ascending order. Then, it iterates over the sorted list, checking the difference between each element and the previous one. If the difference is less than the given threshold, it immediately returns True. If it finishes checking all elements without finding any close ones, it returns False.
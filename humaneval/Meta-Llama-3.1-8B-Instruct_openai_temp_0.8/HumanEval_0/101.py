```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered 'not close'.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to make it easier to check for close elements
    for i in range(1, len(numbers)):  # Iterate over the list starting from the second element
        if numbers[i] - numbers[i - 1] < threshold:  # Check if the current element is close to the previous one
            return True  # If it is, return True immediately
    return False  # If we've checked all elements and haven't found any close pairs, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in the given list are closer to each other than the specified threshold. It sorts the list first to make it easier to check for close elements, and then iterates over the list to check for close pairs. If it finds any close pair, it returns `True` immediately. If it checks all elements without finding any close pairs, it returns `False`.
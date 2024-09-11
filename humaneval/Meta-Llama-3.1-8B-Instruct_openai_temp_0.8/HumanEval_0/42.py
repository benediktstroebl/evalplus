```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of float numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if two numbers are closer than the given threshold, False otherwise.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # Check if the difference between the current and previous number is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # If it is, return True
            return True

    # If no such pair is found, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if any two numbers are closer than the given threshold. If such a pair is found, it returns `True`; otherwise, it returns `False`. The example usage demonstrates how to use this function with the provided test cases.
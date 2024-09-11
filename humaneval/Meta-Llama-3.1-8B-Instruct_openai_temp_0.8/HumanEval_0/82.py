```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered "close".

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # If the list has less than 2 elements, no pairs can be formed, so return False.
    if len(numbers) < 2:
        return False

    # Sort the list in ascending order to make it easier to check for close elements.
    numbers.sort()

    # Iterate over the list to check for close elements.
    for i in range(1, len(numbers)):
        # If the difference between the current element and the previous element is less than the threshold, return True.
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If no close elements were found, return False.
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. It uses a simple iterative approach to check for close elements, and includes example usage at the end.
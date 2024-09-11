```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum difference between two numbers.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """

    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference to a value larger than the threshold
    min_diff = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update it
        if diff < min_diff:
            min_diff = diff

        # If the minimum difference is smaller than the threshold, return True
        if min_diff < threshold:
            return True

    # If no two numbers are closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a given threshold. It sorts the list of numbers and then iterates over the sorted list, keeping track of the minimum difference between any two numbers. If the minimum difference is smaller than the threshold, it returns `True`; otherwise, it returns `False`.
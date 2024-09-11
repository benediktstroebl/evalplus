```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered not close.

    Returns:
    bool: True if any two numbers are closer to each other than the given threshold, False otherwise.
    """
    # Sort the list of numbers to ensure we're checking adjacent numbers in the correct order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            # If it is, return True immediately
            return True

    # If we've checked all numbers and haven't found any that are close, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers to ensure that we're checking adjacent numbers in the correct order. It then iterates over the sorted list, checking if the difference between the current number and the previous number is less than the given threshold. If it is, it returns True immediately. If it checks all numbers without finding any that are close, it returns False.
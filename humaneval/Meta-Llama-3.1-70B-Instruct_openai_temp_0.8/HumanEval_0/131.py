```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed difference between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, checking the difference between each pair of adjacent numbers
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than or equal to the threshold, return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If we've checked all pairs of numbers and haven't found any that are closer than the threshold, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script defines the `has_close_elements` function as described in the problem statement, along with example usage and docstrings to explain how the function works. The function sorts the list of numbers and then checks the difference between each pair of adjacent numbers, returning `True` as soon as it finds a pair that are closer than the threshold, and `False` otherwise.
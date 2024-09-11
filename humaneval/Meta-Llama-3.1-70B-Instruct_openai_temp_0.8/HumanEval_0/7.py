```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # Return True, because we found two numbers that are closer than the threshold
            return True

    # If we didn't find any two numbers that are closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers in ascending order, and then iterates over the sorted list to check if the difference between any two adjacent numbers is less than the threshold. If such a pair of numbers is found, the function returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`.
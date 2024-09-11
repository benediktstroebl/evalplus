```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum difference required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list and check the difference between each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between any two adjacent numbers is less than or equal to the threshold, we return True
        if numbers[i] - numbers[i-1] <= threshold:
            return True

    # If we have checked all pairs of adjacent numbers and haven't found any that are closer than the threshold, we return False
    return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds any pair of numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any that are closer than the threshold, it returns `False`.
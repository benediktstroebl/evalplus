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
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # We start from the second number (index 1) to compare with the previous number
        if i > 0:
            # If the difference between the current number and the previous number is less than the threshold, we return True
            if num - numbers[i-1] < threshold:
                return True

    # If we have iterated over the entire list and haven't found any two numbers closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. It sorts the list of numbers and then iterates over the list, comparing each number with its predecessor to check if the difference is less than the threshold. If it finds two numbers closer than the threshold, it returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate its usage.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if two numbers are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(1, len(numbers)):
        # If the difference between two adjacent elements is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If no pair of close elements is found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a specified threshold. It sorts the list and then iterates over the sorted list to check for close elements. If it finds any pair of close elements, it immediately returns `True`. If it doesn't find any pair of close elements after checking the entire list, it returns `False`. The script also includes test cases to demonstrate the function's behavior.
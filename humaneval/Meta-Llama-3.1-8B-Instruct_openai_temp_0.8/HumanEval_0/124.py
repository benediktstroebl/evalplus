```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers for them to be considered not close.

    Returns:
    bool: True if two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i-1] < threshold:
            # If it is, return True
            return True

    # If we have iterated over the entire list and haven't found any two numbers that are closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if two numbers in the list are closer than the threshold, and `False` otherwise. The function sorts the list of numbers and then iterates over it, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it returns `True`. If it iterates over the entire list without finding any such pair, it returns `False`. The script also includes test cases to demonstrate the function's behavior.
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
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each number, we check if the difference between it and the next number
        # is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # If we find a pair of numbers that are closer than the threshold, we return True
            return True

    # If we have iterated over the entire list and not found any pairs of numbers that
    # are closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer to each other than the threshold, and `False` otherwise. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it returns `True`. If it iterates over the entire list without finding any such pairs, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.
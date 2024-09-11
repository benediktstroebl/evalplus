```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list to find any two numbers closer than the threshold
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than or equal to the threshold, return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If we have iterated over the entire list and found no two numbers closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script sorts the list of numbers in ascending order and then iterates over the list to find any two numbers closer than the threshold. If it finds such a pair, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`.
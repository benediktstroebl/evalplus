```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): The list of numbers to check.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i in range(len(numbers) - 1):
        # For each number, we check if the difference with the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If we find a pair of numbers closer than the threshold, we immediately return True
            return True

    # If we have checked all pairs of numbers and haven't found any closer than the threshold, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script works by first sorting the list of numbers. Then it iterates over the sorted list, checking the difference between each number and the next one. If it finds a pair of numbers with a difference less than the threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any closer than the threshold, it returns `False`.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # For each number, we check the difference with the previous number
        if numbers[i] - numbers[i-1] < threshold:
            # If the difference is less than the threshold, we return True
            return True

    # If we have checked all numbers and haven't found any closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This Python function sorts the input list of numbers and then iterates over the sorted list, checking the difference between each number and its predecessor. If it finds a difference less than the given threshold, it returns `True`; otherwise, it returns `False`.
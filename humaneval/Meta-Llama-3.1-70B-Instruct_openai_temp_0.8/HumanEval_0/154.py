```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # For the first number, there is no previous number to compare with, so we skip it
        if i == 0:
            continue
        # For each number, we calculate the difference with the previous number
        difference = num - numbers[i-1]
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we have iterated over the entire list and not found any pair of numbers closer than the threshold, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list, calculating the difference between each number and the previous number. If it finds a pair of numbers with a difference less than or equal to the threshold, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.
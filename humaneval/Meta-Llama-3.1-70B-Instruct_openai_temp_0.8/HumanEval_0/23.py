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

    # Then, we iterate over the sorted list with the index and value
    for i in range(len(numbers) - 1):
        # For each number, we check the difference with the next number
        if numbers[i + 1] - numbers[i] < threshold:
            # If the difference is less than the threshold, we return True
            return True

    # If we have checked all numbers and haven't found any that are closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer to each other than a given threshold. It does this by sorting the list and then iterating over it, checking the difference between each number and the next one. If it finds a difference that is less than the threshold, it immediately returns `True`. If it checks all numbers without finding any that are closer than the threshold, it returns `False`. The script also includes two test cases to demonstrate its usage.
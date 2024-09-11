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
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no two numbers are closer than the threshold, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script works by first sorting the list of numbers. Then, it iterates over the sorted list and checks if the difference between two adjacent numbers is less than the threshold. If such a pair is found, it immediately returns `True`. If no such pair is found after iterating over the entire list, it returns `False`.
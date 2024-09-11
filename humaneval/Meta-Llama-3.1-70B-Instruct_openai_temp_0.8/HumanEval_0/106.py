```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False  # Need at least two numbers to compare

    numbers.sort()  # Sort the list to efficiently find close numbers

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] < threshold:
            return True  # Found two numbers closer than the threshold

    return False  # No two numbers were closer than the threshold


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
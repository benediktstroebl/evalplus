```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating-point numbers.
        threshold (float): The minimum distance between two numbers to be considered as "close".

    Returns:
        bool: True if there are two numbers closer to each other than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to simplify the comparison of adjacent elements
    for i in range(1, len(numbers)):
        # Check if the difference between two adjacent elements is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.2, 3.4, 5.6], 0.2))  # False
print(has_close_elements([1.2, 3.3, 5.5, 7.7], 0.2))  # True
```
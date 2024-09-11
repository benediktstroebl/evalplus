```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers: List of floats
        threshold: Minimum difference required between two numbers

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise
    """
    numbers.sort()  # Sort the list to bring close numbers together
    for i in range(1, len(numbers)):  # Iterate over the sorted list
        if numbers[i] - numbers[i-1] < threshold:  # Check if the difference is less than threshold
            return True  # If difference is less than threshold, return True
    return False  # If no two numbers are closer than threshold, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list, and then checks each pair of adjacent numbers to see if their difference is less than the threshold. If it finds such a pair, it immediately returns `True`. If it checks all pairs without finding one that meets the condition, it returns `False`.
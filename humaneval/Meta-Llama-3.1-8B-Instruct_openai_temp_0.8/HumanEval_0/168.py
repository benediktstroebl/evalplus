```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): A float value used to check the closeness.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sorting the list to ensure that we're checking adjacent elements
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] <= threshold:
            return True  # If we find two adjacent elements closer than the threshold, return True
    return False  # If we've checked all pairs and haven't returned True, no two numbers are closer than the threshold

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses a simple sorting approach to ensure that adjacent elements are checked for closeness. It iterates over the sorted list, checking each pair of adjacent elements for closeness. If any pair is found to be closer than the threshold, the function immediately returns `True`. If it checks all pairs without finding any closer than the threshold, it returns `False`.
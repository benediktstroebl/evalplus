```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True  # If it is, return True immediately

    # If the function hasn't returned True after checking all pairs of numbers, return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed")
else:
    print("Test case 2 passed")
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if any two numbers are closer than the threshold. If it finds such a pair, it returns `True` immediately. If it checks all pairs of numbers without finding any closer than the threshold, it returns `False`. The script also includes test cases to verify that the function behaves correctly.
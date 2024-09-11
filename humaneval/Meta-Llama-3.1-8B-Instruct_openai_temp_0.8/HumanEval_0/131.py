```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered "far enough".

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, comparing each number with its neighbours
    for i in range(1, len(numbers) - 1):
        # Check if the current number and the next number are within the threshold
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True  # If so, return True immediately

    return False  # If no close elements were found, return False


# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value as input. It sorts the list in ascending order and then iterates over the sorted list, checking each number with its neighbours to see if they are within the threshold. If it finds two numbers that are within the threshold, it returns `True` immediately. If it checks all pairs of numbers without finding any within the threshold, it returns `False`. The script also includes test cases to demonstrate the function's behaviour.
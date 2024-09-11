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
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference as infinity
    min_diff = float('inf')

    # Iterate over the sorted list to find the minimum difference
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        # Update the minimum difference if a smaller difference is found
        if diff < min_diff:
            min_diff = diff

    # Return True if the minimum difference is less than the threshold, False otherwise
    return min_diff < threshold


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer to each other than a given threshold. The function first sorts the list of numbers in ascending order, then iterates over the sorted list to find the minimum difference between any two numbers. If the minimum difference is less than the threshold, the function returns `True`; otherwise, it returns `False`. The script includes two test cases to demonstrate the function's behavior.
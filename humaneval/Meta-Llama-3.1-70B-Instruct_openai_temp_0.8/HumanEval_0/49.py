```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference as infinity
    min_diff = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is less than the threshold and the minimum difference, update the minimum difference
        if diff < threshold and diff < min_diff:
            min_diff = diff

    # If the minimum difference is less than the threshold, return True
    # Otherwise, return False
    return min_diff < threshold


# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script sorts the list of numbers and then iterates over the sorted list to find the minimum difference between any two numbers. If the minimum difference is less than the threshold, the function returns True; otherwise, it returns False.
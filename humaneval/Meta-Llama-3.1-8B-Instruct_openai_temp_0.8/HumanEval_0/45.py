```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, return True immediately
            return True

    # If we've checked all pairs of numbers and haven't found any that are close, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed: expected False")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed: expected True")
else:
    print("Test case 2 passed")
```

This script will check if any two numbers in the given list are closer than the specified threshold. It does this by first sorting the list of numbers, then iterating over the sorted list and checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it immediately returns True. If it checks all pairs of numbers without finding any that are close, it returns False.
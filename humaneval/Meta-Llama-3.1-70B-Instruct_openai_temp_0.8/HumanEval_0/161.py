```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, are any two numbers closer to each other than the given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are any two numbers closer than the threshold, False otherwise.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference as infinity
    min_diff = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous number
        diff = numbers[i] - numbers[i-1]
        
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)

        # If the minimum difference is less than or equal to the threshold, return True
        if min_diff <= threshold:
            return True

    # If we have iterated over the entire list and not found any two numbers closer than the threshold, return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed")
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed")
```

This script defines the `has_close_elements` function as specified, along with test cases to verify its correctness. It sorts the list of numbers, then iterates over the sorted list to find the minimum difference between any two adjacent numbers. If the minimum difference is less than or equal to the threshold, it returns `True`; otherwise, it returns `False`.
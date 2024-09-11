```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if any two numbers in the list are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, comparing each number with its previous one
    for i in range(1, len(numbers)):
        # If the difference between the current and previous numbers is smaller than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # Return True, because we found two numbers that are closer than the threshold
            return True

    # If we've iterated over the entire list and haven't found any close numbers, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Expected False for [1.0, 2.0, 3.0] and threshold 0.5"

if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Expected True for [1.0, 2.8, 3.0, 4.0, 5.0, 2.0] and threshold 0.3"
```
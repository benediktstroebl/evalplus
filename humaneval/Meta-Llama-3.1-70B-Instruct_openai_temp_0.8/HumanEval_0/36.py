```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # We only need to check the next number in the list, because the list is sorted
        if i < len(numbers) - 1:
            # If the difference between the current number and the next number is less than the threshold, we return True
            if numbers[i + 1] - num < threshold:
                return True

    # If we have checked all numbers and haven't found any that are closer than the threshold, we return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Test case 1 failed"
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Test case 2 failed"
if not has_close_elements([1.0, 1.1, 2.0, 3.0], 0.2):
    assert False, "Test case 3 failed"
if has_close_elements([1.0, 2.0, 3.0, 4.0], 1.0):
    assert False, "Test case 4 failed"
```
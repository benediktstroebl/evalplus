```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # We iterate over the sorted list, checking the difference between each pair of adjacent numbers
    for i in range(len(numbers) - 1):
        # If we find a pair of numbers with a difference less than or equal to the threshold, we return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If we've checked all pairs of numbers and haven't found any with a difference less than or equal to the threshold, we return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Test 1 failed"
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Test 2 failed"
if has_close_elements([10.0, 20.0, 30.0], 5.0):
    assert False, "Test 3 failed"
if has_close_elements([1.0, 1.1, 2.0], 0.5):
    assert True, "Test 4 failed"
```
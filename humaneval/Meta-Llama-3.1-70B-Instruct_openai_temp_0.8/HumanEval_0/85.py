```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, checking the difference between each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than or equal to the threshold, return True
        if numbers[i] - numbers[i-1] <= threshold:
            return True

    # If no pairs of numbers with a difference less than or equal to the threshold were found, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Test 1 failed"
else:
    assert True

if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Test 2 failed"
else:
    assert True
```
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
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each pair of adjacent numbers, we check if the difference is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, we immediately return True
            return True

    # If we've checked all pairs of adjacent numbers and haven't returned True, we return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, f"Expected False, got {has_close_elements([1.0, 2.0, 3.0], 0.5)}"
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert True, f"Expected True, got {has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)}"
```
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
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # Return True, indicating that two numbers are closer than the threshold
            return True

    # If the function hasn't returned True by now, it means no two numbers are closer than the threshold
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Test failed: has_close_elements([1.0, 2.0, 3.0], 0.5) should return False"
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Test failed: has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) should return True"

print("All test cases passed.")
```
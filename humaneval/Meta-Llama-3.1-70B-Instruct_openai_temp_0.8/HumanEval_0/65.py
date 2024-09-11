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

    # Then, we iterate over the sorted list with the index
    for i in range(len(numbers) - 1):
        # For each number, we check the difference with the next number
        if numbers[i + 1] - numbers[i] < threshold:
            # If the difference is less than the threshold, we return True
            return True

    # If we have iterated over the entire list and not found any close elements, we return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Expected False, got True"
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Expected True, got False"
print("All test cases pass")
```

This script defines the `has_close_elements` function, which sorts a list of numbers and checks the difference between each pair of adjacent numbers. If any pair is closer than the given threshold, it immediately returns `True`. If no such pair is found after checking the entire list, it returns `False`.

The script also includes two test cases to verify the function's correctness. If either test fails, it prints an error message. If both tests pass, it prints "All test cases pass".
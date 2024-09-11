```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum difference between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # We only need to check the next number in the list
        if i < len(numbers) - 1:
            # If the difference between the current number and the next number is less than or equal to the threshold
            if numbers[i + 1] - num <= threshold:
                # We return True, indicating that there are two numbers closer than the threshold
                return True

    # If we've iterated over the entire list and haven't found any numbers closer than the threshold
    # We return False, indicating that no such pair exists
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
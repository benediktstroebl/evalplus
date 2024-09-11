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
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, comparing each number with its next neighbor
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # Return True, because we've found two numbers that are closer than the threshold
            return True

    # If we've iterated over the entire list without finding any close numbers, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # For the last number, there's no next number to compare with, so we break the loop
        if i == len(numbers) - 1:
            break
        # We calculate the difference between the current number and the next number
        difference = numbers[i + 1] - num
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we've iterated over the entire list and haven't found a pair of numbers closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
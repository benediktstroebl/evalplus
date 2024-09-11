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
        bool: True if any two numbers in the list are closer to each other than the threshold,
              False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list to check the distance between adjacent numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than or equal to the threshold,
        # we return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If we have checked all adjacent numbers and haven't found any that are closer than the threshold,
    # we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4], 0.1))  # True
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4], 0.01))  # False
```
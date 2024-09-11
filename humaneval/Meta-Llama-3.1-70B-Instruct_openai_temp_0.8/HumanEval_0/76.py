```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list to compare adjacent numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # We return True, indicating that there are two numbers closer than the threshold
            return True

    # If we've iterated over the entire list without finding any close numbers, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5], 0.2))  # True
print(has_close_elements([1.0, 10.0, 20.0, 30.0, 40.0, 50.0], 5.0))  # False
```
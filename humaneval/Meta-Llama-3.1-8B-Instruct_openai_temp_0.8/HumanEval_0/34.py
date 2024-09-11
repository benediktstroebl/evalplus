```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of numbers to check.
        threshold (float): The minimum difference required between two numbers.

    Returns:
        bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If the difference is less than the threshold, return True
            return True

    # If no two numbers are closer to each other than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 2.0, 4.0, 5.0], 1.0))  # False
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4], 0.3))  # True
```
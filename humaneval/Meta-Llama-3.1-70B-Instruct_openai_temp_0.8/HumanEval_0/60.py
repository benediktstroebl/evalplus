```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of numbers to check.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list, checking the difference between adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i] - numbers[i-1] < threshold:
            return True

    # If no pairs of numbers are closer than the threshold, return False
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```
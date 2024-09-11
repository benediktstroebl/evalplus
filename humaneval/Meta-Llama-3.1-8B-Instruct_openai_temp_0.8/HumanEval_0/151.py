```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list in ascending order
    numbers.sort()

    # Iterate over the sorted list, considering each pair of adjacent numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than or equal to the threshold
        if abs(numbers[i + 1] - numbers[i]) <= threshold:
            # Return True immediately, because the condition is met
            return True

    # If the loop completes without finding any adjacent numbers closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list, and then checks each pair of adjacent numbers to see if their difference is less than or equal to the threshold. If it finds any pair of adjacent numbers closer than the threshold, it immediately returns True. If it checks all pairs without finding any closer than the threshold, it returns False.
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to make the comparison more efficient
    for i in range(1, len(numbers)):  # Iterate over the sorted list
        if numbers[i] - numbers[i-1] < threshold:  # Check if the difference between two consecutive numbers is less than the threshold
            return True  # If it is, return True immediately
    return False  # If the loop completes without finding any close elements, return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
```

This script first sorts the list of numbers to make the comparison more efficient. Then it iterates over the sorted list, checking if the difference between two consecutive numbers is less than the threshold. If it is, the function returns True immediately. If the loop completes without finding any close elements, the function returns False.
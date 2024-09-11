```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no close elements are found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of float numbers and a threshold as input. It sorts the list and then iterates over the sorted list to check if any two adjacent numbers are closer than the threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The test cases are also included to demonstrate the usage of the function.
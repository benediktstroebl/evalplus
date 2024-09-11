```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate over the list of numbers
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous one is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    
    # If we've checked all numbers and haven't found any close elements, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer to each other than the threshold, and `False` otherwise. The function first sorts the list of numbers, then checks each pair of adjacent numbers to see if they are close. If it finds any pair that is close, it immediately returns `True`. If it checks all pairs without finding any close ones, it returns `False`. The script also includes example usage of the function with the provided test cases.
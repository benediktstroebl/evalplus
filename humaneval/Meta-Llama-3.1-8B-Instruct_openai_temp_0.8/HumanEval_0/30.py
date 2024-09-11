```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to make it easier to check for close elements
    for i in range(1, len(numbers)):  # Start from the second element
        if numbers[i] - numbers[i-1] < threshold:  # Check if the current element and the previous element are closer than the threshold
            return True
    return False  # If we checked all elements and didn't find any close pair, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in the given list are closer than the specified threshold. It uses a simple and efficient algorithm to solve this problem. The function sorts the list first, then iterates over the list to check for close elements. If it finds any close pair, it immediately returns `True`. If it checks all elements and doesn't find any close pair, it returns `False`. The script also includes test cases to demonstrate the function's behavior.
### Solution: Check for Close Elements in a List of Numbers

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order
    for i in range(1, len(numbers)):  # Iterate over the sorted list
        if numbers[i] - numbers[i - 1] <= threshold:  # Check if current number is within the threshold of the previous number
            return True  # If yes, return True
    return False  # If no such pair is found, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a distance threshold as input. It sorts the list in ascending order and then iterates over the sorted list to check if any two adjacent numbers are within the specified threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`.
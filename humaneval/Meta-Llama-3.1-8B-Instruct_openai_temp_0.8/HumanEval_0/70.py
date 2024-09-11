```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating-point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order
    for i in range(1, len(numbers)):  # Iterate over the sorted list
        if numbers[i] - numbers[i-1] < threshold:  # Check if the difference is less than threshold
            return True
    return False  # If no pair of numbers is closer than threshold, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating-point numbers and a threshold as input. It sorts the list in ascending order, then iterates over the sorted list, checking if the difference between each pair of adjacent numbers is less than the threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`. The script also includes two test cases to demonstrate the function's behavior.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if any two numbers are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate through the list with two pointers
    for i in range(len(numbers) - 1):
        # If the difference between consecutive numbers is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True
    
    # If no close elements are found
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold. It sorts the list, then iterates through it with two pointers. If the difference between consecutive numbers is less than the threshold, it immediately returns `True`. If it iterates through the entire list without finding any close elements, it returns `False`.
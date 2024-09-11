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
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list, checking the distance between each pair of adjacent numbers
    for i in range(1, len(sorted_numbers)):
        # If the distance between the current number and the previous number is less than the threshold, return True
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            return True
    
    # If no pair of adjacent numbers are closer than the threshold, return False
    return False


# Example use cases:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which takes a list of numbers and a threshold as input, sorts the list, and then checks the distance between each pair of adjacent numbers. If any pair of adjacent numbers are closer than the threshold, the function returns `True`; otherwise, it returns `False`. The example use cases at the end demonstrate the function's behavior with different inputs.
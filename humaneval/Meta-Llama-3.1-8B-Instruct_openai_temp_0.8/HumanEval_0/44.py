```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to compare each pair of adjacent numbers
    for i in range(1, len(sorted_numbers)):
        # Check if the difference between the current number and the previous one is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i-1] < threshold:
            # If it is, return True
            return True
    
    # If no pair of numbers is closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list, then iterates over the sorted list to compare each pair of adjacent numbers. If it finds a pair of numbers whose difference is less than the threshold, it returns `True`. If no such pair is found after checking all pairs, it returns `False`. The test cases at the end demonstrate the function's behavior with different inputs.
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
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # Return True as we have found two numbers closer than the threshold
            return True
    
    # If we have iterated over the entire list without finding two numbers closer than the threshold
    # Return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if any two adjacent numbers are closer than the threshold. If such a pair is found, the function returns `True`. Otherwise, it returns `False`. The script includes example usage to demonstrate the function's behavior.
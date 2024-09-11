```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers to make it easier to compare adjacent elements
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Check if the current number and the previous number are closer than the threshold
        if abs(numbers[i] - numbers[i - 1]) < threshold:
            # If they are, return True immediately
            return True
    
    # If we've iterated over the entire list and haven't found any adjacent numbers that are closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value. It sorts the list and then iterates over it, checking if any two adjacent numbers are closer than the threshold. If it finds such a pair, it returns `True`. If it iterates over the entire list without finding any such pair, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.
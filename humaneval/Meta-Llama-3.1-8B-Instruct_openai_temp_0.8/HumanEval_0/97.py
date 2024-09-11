```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # If the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            # Return True, because we found two numbers that are closer to each other than the threshold
            return True
    
    # If we reached this point, it means that we didn't find any two numbers that are closer to each other than the threshold
    # So, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer to each other than the threshold, it immediately returns `True`. If it reaches the end of the list without finding any such pair, it returns `False`. The script also includes test cases to demonstrate the function's behavior.
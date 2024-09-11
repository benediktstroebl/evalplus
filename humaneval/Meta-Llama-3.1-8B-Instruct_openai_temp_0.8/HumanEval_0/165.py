```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): A minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Check if the difference between current number and previous number is less than threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True
    
    # If no two numbers are closer than threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers, then iterates over the sorted list to check if any two numbers are closer than the given threshold. If it finds two numbers that are closer than the threshold, it immediately returns `True`. If it iterates over the entire list without finding any two numbers that are closer than the threshold, it returns `False`. The script also includes test cases to demonstrate the function's behavior.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): List of floating point numbers.
    threshold (float): Threshold value to check if any two numbers are closer to each other.

    Returns:
    bool: True if any two numbers are closer to each other, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to check if any two adjacent numbers are closer than the threshold
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] - sorted_numbers[i-1] <= threshold:
            return True
    
    # If no two adjacent numbers are closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers, then checks each pair of adjacent numbers to see if they are closer than the given threshold. If any pair of adjacent numbers is closer than the threshold, it immediately returns `True`. If it checks all pairs without finding any closer than the threshold, it returns `False`.
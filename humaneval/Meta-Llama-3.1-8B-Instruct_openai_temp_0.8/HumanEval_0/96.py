### Close Elements Checker

#### Problem Description

Check if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Solution

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
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list
    for i in range(len(sorted_numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            return True
    
    # If no close elements are found, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list and then checks each pair of adjacent numbers to see if they are closer than the threshold. If it finds a pair that is closer, it immediately returns `True`. If it checks all pairs without finding any that are closer, it returns `False`.
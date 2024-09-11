```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    
    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list in ascending order
    numbers.sort()

    # Iterate over the sorted list with indices
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True  # If so, return True

    # If no such pair is found, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list and then iterates over it with indices to check if the difference between each pair of adjacent numbers is less than the threshold. If such a pair is found, it immediately returns `True`. If no such pair is found after checking all numbers, it returns `False`.
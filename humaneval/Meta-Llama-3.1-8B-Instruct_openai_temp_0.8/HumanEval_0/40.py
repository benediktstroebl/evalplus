```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the list, considering each pair of adjacent numbers
    for i in range(len(numbers) - 1):
        # Calculate the distance between the current and next numbers
        distance = numbers[i + 1] - numbers[i]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True

    # If we've checked all pairs of numbers and haven't found any closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function sorts the list of numbers and then iterates over the list, considering each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any closer than the threshold, it returns `False`. The script also includes example usage of the function.
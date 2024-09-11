```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than threshold, False otherwise.
    """
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # Calculate the distance between current and previous number
        distance = sorted_numbers[i] - sorted_numbers[i - 1]
        
        # If the distance is less than threshold, return True
        if distance < threshold:
            return True

    # If no two numbers are closer than threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers, then iterates over the sorted list to check the distance between each pair of adjacent numbers. If it finds a pair of numbers with a distance less than the threshold, it returns `True`. If it checks all pairs of numbers without finding any closer than the threshold, it returns `False`. The script includes example usage to demonstrate how to call the function.
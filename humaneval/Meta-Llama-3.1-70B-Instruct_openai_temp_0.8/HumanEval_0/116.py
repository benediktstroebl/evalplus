```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each number, we check the difference with the next number
        if numbers[i + 1] - numbers[i] < threshold:
            # If the difference is less than the threshold, we return True
            return True
    
    # If we have iterated over the entire list and not found any close elements, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which checks if any two numbers in a list are closer to each other than a given threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each number and the next one. If it finds a difference that is less than the threshold, it returns `True`. If it iterates over the entire list without finding any close elements, it returns `False`.
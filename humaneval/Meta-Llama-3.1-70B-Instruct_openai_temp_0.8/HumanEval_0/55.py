```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # We then iterate through the sorted list of numbers
    for i in range(1, len(numbers)):
        # For each number, we calculate the difference between it and the previous number
        difference = numbers[i] - numbers[i - 1]
        
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we have iterated through the entire list and not found any two numbers closer than the threshold,
    # we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns True if there are any two numbers in the list that are closer to each other than the threshold. It does this by sorting the list of numbers and then iterating through the sorted list, checking the difference between each number and the previous one. If it finds a difference that is less than or equal to the threshold, it returns True. If it iterates through the entire list without finding any such difference, it returns False.
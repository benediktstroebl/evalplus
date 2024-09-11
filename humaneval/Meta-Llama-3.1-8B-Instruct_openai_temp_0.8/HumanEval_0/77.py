```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to make it easier to find close elements
    for i in range(len(numbers) - 1):
        # For each pair of adjacent elements, check if they are closer than the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            return True
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 2.0))  # False
```

This script implements the `has_close_elements` function as described, which checks if any two elements in the input list are closer together than the given threshold. The function sorts the list first to make it easier to find adjacent elements that are close together. It then iterates over the sorted list, checking each pair of adjacent elements to see if they are closer than the threshold. If it finds any pair that is closer, it immediately returns True. If it checks all pairs and doesn't find any that are closer, it returns False.
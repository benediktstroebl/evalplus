```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): Maximum allowed difference between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Check if the list has less than two elements
    if len(numbers) < 2:
        return False

    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(1, len(numbers)):
        # If the difference between the current element and the previous one is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If no close elements are found, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

In this code, we sort the list of numbers and then iterate over it to check each pair of adjacent elements. If we find a pair with a difference less than the threshold, we immediately return True. If we reach the end of the list without finding any close elements, we return False.
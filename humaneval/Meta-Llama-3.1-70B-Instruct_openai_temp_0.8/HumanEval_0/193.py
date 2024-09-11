```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # We calculate the distance between each pair of adjacent numbers
        distance = numbers[i + 1] - numbers[i]
        
        # If we find a pair of numbers with a distance less than the threshold, we return True
        if distance < threshold:
            return True

    # If we don't find any pair of numbers with a distance less than the threshold, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the input list of numbers, then iterates over the sorted list to check the distance between each pair of adjacent numbers. If it finds a pair of numbers with a distance less than the given threshold, it immediately returns `True`. If it checks all pairs without finding any with a distance less than the threshold, it returns `False`.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and the value
    for i, num in enumerate(numbers):
        # We only need to check the next number in the list
        if i < len(numbers) - 1:
            # If the difference between the current number and the next number is less than the threshold
            if abs(num - numbers[i + 1]) < threshold:
                # We return True, because we found two numbers that are closer than the threshold
                return True

    # If we didn't find any two numbers that are closer than the threshold, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a given threshold. The function sorts the list of numbers and then iterates over the list, checking the difference between each number and the next one. If it finds two numbers that are closer than the threshold, it returns `True`. If it doesn't find any such numbers, it returns `False`.
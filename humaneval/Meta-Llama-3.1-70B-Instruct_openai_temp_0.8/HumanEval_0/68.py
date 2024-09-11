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
        bool: True if two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers
    numbers.sort()

    # Then, we iterate over the sorted list
    for i in range(1, len(numbers)):
        # For each number, we check if the difference between it and the previous number is less than the threshold
        if abs(numbers[i] - numbers[i-1]) < threshold:
            # If we find such a pair, we immediately return True
            return True

    # If we've iterated over the entire list and haven't found any close elements, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` which takes a list of floating point numbers and a threshold as input. It checks if any two numbers in the list are closer to each other than the given threshold. The function returns `True` if such a pair is found, and `False` otherwise. The script also includes example usage of the function.
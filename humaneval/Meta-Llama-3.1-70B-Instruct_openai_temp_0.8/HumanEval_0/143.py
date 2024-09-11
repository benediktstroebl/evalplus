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

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    numbers = sorted(numbers)  # Sort the list of numbers in ascending order
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] <= threshold:  # Check if the difference between two adjacent numbers is less than or equal to the threshold
            return True  # If the difference is less than or equal to the threshold, return True
    return False  # If the function hasn't returned True after iterating over the entire list, return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
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
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # Return True, indicating that two numbers are closer than the threshold
            return True

    # If no two numbers are closer than the threshold, return False
    return False


# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function first sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If the difference is less than or equal to the threshold, the function returns `True`; otherwise, it returns `False`. The script includes example usage of the function to demonstrate its behavior.
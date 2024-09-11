```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers for them to be considered close.

    Returns:
    bool: True if any two numbers are closer than threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, comparing each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            # Return True, indicating that there are two numbers closer than the threshold
            return True

    # If no pairs of numbers closer than the threshold are found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list, then iterates over the sorted list, comparing each pair of adjacent numbers. If it finds a pair of numbers whose difference is less than the threshold, it returns `True`. If it exhausts the entire list without finding a pair of close numbers, it returns `False`. The test cases provided in the docstring are demonstrated at the end of the script.
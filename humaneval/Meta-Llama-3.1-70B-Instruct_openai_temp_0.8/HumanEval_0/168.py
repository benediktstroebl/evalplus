```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum difference between two numbers.

    Returns:
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each number, we check if the difference between it and the next number
        # is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # If we find such a pair of numbers, we immediately return True
            return True

    # If we have iterated over the entire list and haven't found any such pairs,
    # we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the function `has_close_elements` which checks if any two numbers in a given list are closer to each other than a given threshold. It does this by sorting the list of numbers and then iterating over the list to check the differences between adjacent numbers. If it finds any pair of numbers with a difference less than or equal to the threshold, it immediately returns `True`. If it doesn't find any such pairs after iterating over the entire list, it returns `False`.
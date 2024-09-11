```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum difference between two numbers.

    Returns:
    bool: True if there are two numbers closer to each other than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False  # List must contain at least two elements

    numbers.sort()  # Sort the list to efficiently compare adjacent elements

    for i in range(1, len(numbers)):
        # Check if the difference between two adjacent numbers is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It checks if there are any two numbers in the list that are closer to each other than the given threshold. The function returns `True` if such a pair is found, and `False` otherwise.

The function first checks if the list contains at least two elements, in which case it returns `False`. Then it sorts the list to efficiently compare adjacent elements. It iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair with a difference less than the threshold, it immediately returns `True`. If it checks all pairs without finding a match, it returns `False`.

The script includes two test cases at the end to verify that the function works correctly.
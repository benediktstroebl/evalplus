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
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i in range(len(numbers) - 1):
        # For each number, we check if the difference between it and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If we find a pair of numbers that are closer than the threshold, we immediately return True
            return True

    # If we iterate over the entire list and don't find any pairs of numbers that are closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which checks if any two numbers in a given list are closer to each other than a given threshold. It uses a simple iterative approach, sorting the list first and then checking each pair of adjacent numbers. The function returns `True` as soon as it finds a pair of numbers that are closer than the threshold, and `False` otherwise. The script also includes two test cases to demonstrate the function's behavior.
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
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers. This is because we want to compare adjacent
    # numbers in the list, which will have the smallest difference.
    numbers.sort()

    # We iterate over the sorted list of numbers.
    for i in range(len(numbers) - 1):
        # For each number, we calculate the difference with the next number.
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, we return True.
        if difference <= threshold:
            return True

    # If we have iterated over the entire list and haven't found any two numbers with
    # a difference less than or equal to the threshold, we return False.
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
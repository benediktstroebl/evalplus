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
    # First, we sort the list of numbers. This is because we want to compare adjacent
    # numbers, and if the list is sorted, we know that the closest numbers will be
    # next to each other.
    numbers.sort()

    # Then, we iterate over the sorted list of numbers. We use the zip function to
    # get both the current number and the next number in the list.
    for current, next_number in zip(numbers, numbers[1:]):
        # For each pair of numbers, we calculate the difference between them.
        difference = abs(current - next_number)
        
        # If the difference is less than or equal to the threshold, we return True.
        if difference <= threshold:
            return True

    # If we have iterated over the entire list and not found any pairs of numbers
    # that are closer than the threshold, we return False.
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
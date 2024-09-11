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
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # For each number, we calculate the difference between it and the previous number
        difference = numbers[i] - numbers[i - 1]
        
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we've iterated over the entire list and haven't found any numbers closer than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the input list of numbers, then iterates over the sorted list to check if any two consecutive numbers are closer than the given threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`.
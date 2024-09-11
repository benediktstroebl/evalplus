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
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If no pairs of numbers with a difference less than or equal to the threshold
    # were found, return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script first sorts the list of numbers in ascending order. Then, it iterates over the sorted list and calculates the difference between each pair of adjacent numbers. If it finds a pair of numbers with a difference less than or equal to the threshold, it immediately returns True. If it doesn't find any such pairs after iterating over the entire list, it returns False.
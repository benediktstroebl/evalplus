```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed difference between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize a variable to store the result
    has_close = False

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each number, calculate the difference with the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, update the result
        if difference <= threshold:
            has_close = True
            # We can break the loop as soon as we find a pair of close numbers
            break

    return has_close


# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function sorts the list of numbers and then iterates over the sorted list, calculating the difference between each number and the next one. If it finds a difference that is less than or equal to the threshold, it returns `True`. If it doesn't find any such difference after iterating over the entire list, it returns `False`.
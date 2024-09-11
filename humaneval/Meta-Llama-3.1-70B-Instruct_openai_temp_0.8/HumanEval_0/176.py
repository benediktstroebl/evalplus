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

    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the previous number to the first number in the sorted list
    previous_number = numbers[0]

    # Iterate over the rest of the numbers in the sorted list
    for current_number in numbers[1:]:
        # If the difference between the current number and the previous number is less than the threshold, return True
        if current_number - previous_number < threshold:
            return True
        # Update the previous number for the next iteration
        previous_number = current_number

    # If we have iterated over the entire list and not found any numbers closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which takes a list of numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers, then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers with a difference less than the threshold, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.
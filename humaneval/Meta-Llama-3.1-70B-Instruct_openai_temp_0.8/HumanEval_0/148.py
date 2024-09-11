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

    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the previous number to the first number in the sorted list
    previous_number = numbers[0]

    # Iterate over the sorted list starting from the second number
    for current_number in numbers[1:]:
        # Calculate the absolute difference between the current and previous numbers
        difference = abs(current_number - previous_number)

        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

        # Update the previous number to the current number for the next iteration
        previous_number = current_number

    # If no close elements are found after iterating over the entire list, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating-point numbers and a threshold as input. It sorts the list of numbers in ascending order and then iterates over the sorted list to find any two numbers that are closer than the given threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script also includes example usage to demonstrate the function's behavior.
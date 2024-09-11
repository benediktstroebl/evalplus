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

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference to infinity
    min_diff = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous number
        diff = numbers[i] - numbers[i-1]
        
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff

    # Return True if the minimum difference is less than or equal to the threshold, False otherwise
    return min_diff <= threshold


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a given threshold. It sorts the list of numbers in ascending order and then iterates over the list to find the minimum difference between two consecutive numbers. If the minimum difference is less than or equal to the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes example usage of the function.
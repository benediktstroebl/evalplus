```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize a variable to store the previous number in the sorted list
    prev_num = numbers[0]

    # Iterate over the sorted list starting from the second number
    for num in numbers[1:]:
        # Check if the distance between the current number and the previous number is less than the threshold
        if num - prev_num < threshold:
            # If it is, return True immediately
            return True
        # Otherwise, update the previous number for the next iteration
        prev_num = num

    # If the loop completes without finding any two numbers closer than the threshold, return False
    return False

# Test the function with examples
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which sorts the input list of numbers and then checks each pair of adjacent numbers to see if they are closer than the specified threshold. If it finds any pair that meets this condition, it returns `True`. If it checks all pairs without finding any closer than the threshold, it returns `False`. The script includes docstrings and example usage to clarify its behavior.